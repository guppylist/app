from django.test import TestCase
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from guppylist.contrib.list.models import List, ListProducts
from guppylist.contrib.product.models import Product

class ListTest(TestCase):
    def create(self):
        # Create a user.
        username = 'testuser'

        user = User()
        user.username = username
        user.save()

        # Test user.
        user = User.objects.get(username=username)
        self.assertEqual(user.username, username)

        # Create a list.
        title = 'My Christmas List'
        description = 'This is my list of stuff I want for Christmas.'

        list = List()
        list.user = user
        list.title = title
        list.description = description
        list.save()

        # Test the list.
        list = List.objects.get(user=user, title=title)
        self.assertEqual(list.title, title)
        self.assertEqual(list.description, description)
        self.assertEqual(list.user.username, username)

        # Create products.
        count = 10
        for i in range(0, count):
            asin = 'ASIN-%s' % i
            slug = slugify('this is a Product SLUG %s' % i)

            product = Product()
            product.asin = asin
            product.slug = slug
            product.save()

            # Test the product.
            product = Product.objects.get(slug=slug)
            self.assertEqual(product.asin, asin)
            self.assertEqual(product.slug, slug)

        # Add items to a list.
        for i in range(0, count):
            notes = 'Here are some notes for the list item %s.' % i
            product = Product.objects.get(asin=('ASIN-%s' % i))

            list_products = ListProducts()
            list_products.product = product
            list_products.user = user
            list_products.list = list
            list_products.notes = notes
            list_products.save()

            # Test list item.
            list_products = ListProducts.objects.get(id=list_products.id)
            self.assertEqual(list_products.product.id, product.id)
            self.assertEqual(list_products.list.id, list.id)
            self.assertEqual(list_products.user.id, user.id)
            self.assertEqual(list_products.notes, notes)

        self.assertEqual(len(list.listproducts_set.all()), count)
