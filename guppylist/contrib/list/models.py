from django.conf import settings
from django.db import models
from guppylist.core.models import ContentModel, BaseModel
from guppylist.contrib.product.models import Product

class List(ContentModel):
    description = models.TextField(null=False, blank=False)

    @staticmethod
    def does_product_exist_on_list(user, product):
        exists = False

        # lists = List.objects.get(user=user, product)

    def get_absolute_url(self):
        return '/u/caleb/list/%s' % self.slug

    def product_is_in_list(self):
        return True

class ListProducts(BaseModel):
    product = models.ForeignKey(Product, null=False)
    list = models.ForeignKey(List, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
    claimer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='claimer')
    notes = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)