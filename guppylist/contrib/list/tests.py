import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from guppylist.contrib.list.models import Item

class ListItemTest(TestCase):
    def test_get_metadata(self):
        url = 'http://www.theguardian.com/music/2013/dec/06/bob-dylan-electric-guitar-fender-stratocaster-auction-christies'
        # url = 'http://www.area22guitars.com/boutique-guitar-amps/divided-by-13/divided-by-13-sjt-10-20.html'
        meta = Item.get_metadata(url)

        # user = User()
        # user.password = 'asdf'
        # user.last_login = datetime.datetime.now()
        # user.is_superuser = 0
        # user.username = 'asdfasdf'
        # user.first_name = 'asdf'
        # user.last_name = 'asdf'
        # user.email = 'asdf@asdf.com'
        # user.is_staff = 0
        # user.is_active = 1
        # user.date_joined = datetime.datetime.now()
        # user.about_me = 'asdf asdf asdf'
        # user.facebook_id = 1234567890
        # user.access_token = 'asdf asdfa sdfasd fasd f'
        # user.facebook_name = 'asdf'
        # user.facebook_profile_url = 'asdf'
        # user.website_url = 'asdf'
        # user.blog_url = 'asdf'
        # user.date_of_birth = datetime.datetime.now()
        # user.gender = 'M'
        # user.raw_data = 'asdf'
        # user.facebook_open_graph = 123
        # user.new_token_required = 123
        # user.image = 'asdf'
        # user.state = 'asdf'
        # user.save()

        # item = Item()
        # item.user = user
        # item.url = 'http://www.theguardian.com/music/2013/dec/06/bob-dylan-electric-guitar-fender-stratocaster-auction-christies'
        # item.save()

