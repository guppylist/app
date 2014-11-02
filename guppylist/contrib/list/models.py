import urllib2, cStringIO
from PIL import Image

from django.conf import settings
from django.db import models

from bs4 import BeautifulSoup
from imagekit.models import ImageSpecField
from imagekit.processors import resize, ResizeToFill, Anchor, Thumbnail

from guppylist.core.models import ContentModel, BaseModel

class List(ContentModel):
    description = models.TextField(null=False, blank=False)

    @staticmethod
    def does_product_exist_on_list(user, product):
        exists = False

        # lists = List.objects.get(user=user, product)

    def get_url(self):
        return '/u/%s/list/%s' % (self.user.username, self.slug)

    def product_is_in_list(self):
        return True

class Item(ContentModel):
    url = models.URLField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/items', null=True, blank=True)

    # Imagekit settings.
    image_thumb = ImageSpecField(source='image', processors=[Thumbnail(200)], format='JPEG', options={ 'quality': 80 })

    def get_url(self):
        return '/item/%s' % (self.id)

    @staticmethod
    def get_metadata(url):
        meta = {
            'title': '',
            'description': '',
            'images': [],
        }
        soup =  BeautifulSoup(urllib2.urlopen(url))

        # Get the title.
        title = soup.find('meta', attrs={'property': 'og:title', 'content': True})
        if title:
            meta['title'] = title['content']
        else:
            meta['title'] = soup.title.string

        # Get the description.
        description = soup.find('meta', attrs={'property': 'og:description', 'content': True})
        if description:
            meta['description'] = description['content']
        else:
            description2 = soup.find('meta', attrs={'name': 'description', 'content': True})
            if description2:
                meta['description'] = description2['content']

        # Get the image.
        images = soup.find_all('img')
        for image in images:
            if image.has_attr('src') and image['src'].startswith('http'):
                image_file = cStringIO.StringIO(urllib2.urlopen(image['src']).read())
                image_data = Image.open(image_file)
                image_size = image_data.size
                meta['images'].append({ 'size': (image_size[0] + image_size[1]), 'src': image['src']})

        # Sort image list by size to infer main images.
        meta['images'] = sorted(meta['images'], key=lambda k: k['size'], reverse=True)[0:5]

        return meta


class ListProducts(BaseModel):
    list = models.ForeignKey(List, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
    claimer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='claimer')
    notes = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)