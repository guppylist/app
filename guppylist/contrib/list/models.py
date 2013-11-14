from django.db import models
from guppylist.core.models import ContentModel, BaseModel
from guppylist.contrib.product.models import Product

class List(ContentModel):
    description = models.TextField(null=False, blank=False)

    @staticmethod
    def does_product_exist_on_list(user, product):
        exists = False

        # lists = List.objects.get(user=user, product)

class ListProducts(BaseModel):
    product = models.ForeignKey(Product, null=False)
    list = models.ForeignKey(List, null=False)
    create_date = models.DateTimeField(auto_now_add=True)