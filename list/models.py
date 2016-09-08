import datetime

from django.db import models
from django.contrib.auth.models import User

from core.models import ContentModel, BaseModel


class List(ContentModel):
    description = models.TextField(blank=True)
    items = models.ManyToManyField('ListItem', blank=True)

    @staticmethod
    def list_add_item(list_id, product_id, user_id):
        list = List.objects.get(id=list_id)
        # list.items.append(product_id)


class ListItem(ContentModel):
    notes = models.TextField()
    item_id = models.ForeignKey('Item')


class Item(BaseModel):
    item_id = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
    publish_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Publish')
    image_large = models.URLField()
    image_small = models.URLField()
