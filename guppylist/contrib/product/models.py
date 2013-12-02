from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from amazon.api import AmazonAPI
from guppylist.core.models import BaseModel

class Product(BaseModel):
    asin = models.CharField(max_length=64, null=False, blank=False)
    slug = models.SlugField(max_length=512)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return '/products/%s' % self.slug

    def get_details(self):
        amazon = AmazonAPI(settings.AMAZON_ACCESS_KEY_ID, settings.AMAZON_SECRET_KEY, settings.AMAZON_ASSOCIATE_ID)
        product = amazon.lookup(ItemId=self.asin)
        self.data = product

        return self

    @staticmethod
    def get_product_by_slug(slug):
        product = Product.objects.get(slug=slug)

        amazon = AmazonAPI(settings.AMAZON_ACCESS_KEY_ID, settings.AMAZON_SECRET_KEY, settings.AMAZON_ASSOCIATE_ID)
        prod = amazon.lookup(ItemId=product.asin)
        product.data = prod

        return product

    @staticmethod
    def search(q):
        amazon = AmazonAPI(settings.AMAZON_ACCESS_KEY_ID, settings.AMAZON_SECRET_KEY, settings.AMAZON_ASSOCIATE_ID)
        products = amazon.search_n(48, Keywords=q, SearchIndex='All')
        prods = []

        for product in products:
            try:
                prod = Product.objects.get(asin=product.asin)
            except Exception, e:
                prod = Product()
                prod.asin = product.asin
                prod.slug = slugify('%s %s' % (product.title, product.asin))
                prod.save()

            prod.data = product
            prods.append(prod)

        return prods