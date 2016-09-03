import bottlenose

from bs4 import BeautifulSoup

from django.conf import settings

from core.base import BaseObject


class AmazonApi(BaseObject):
    """
    Abstraction to the Amazon Product Advertising API via the bottlenose library.
    @see https://github.com/lionheart/bottlenose
    """

    @staticmethod
    def instance():
        """
        Get an instance of the Amazon Advertising API.
        :return:
        """
        return bottlenose.Amazon(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY, settings.AWS_ASSOCIATE_TAG)

    @staticmethod
    def search(q):
        api = AmazonApi.instance()
        xml_result = api.ItemSearch(Keywords=q, SearchIndex='All', ResponseGroup='Medium')

        root = BeautifulSoup(xml_result, 'xml')
        print(root)

        products = []
        for item in root.Items.find_all('Item'):
            products.append(Product(item))

        return products


class Product(BaseObject):
    def __init__(self, data):
        self.asin = data.ASIN.string
        self.title = data.ItemAttributes.Title.string
        self.brand = data.ItemAttributes.Manufacturer.string if data.ItemAttributes.Manufacturer else None
        self.category = data.ItemAttributes.Binding.string
        self.image_small = data.SmallImage.URL.string
        self.image_medium = data.MediumImage.URL.string
        self.image_large = data.LargeImage.URL.string
        self.detail_page = data.DetailPageURL.string

