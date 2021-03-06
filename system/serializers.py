from django.contrib.auth.models import User, Group
from rest_framework import serializers

from list.models import List, ListItem


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ProductSerializer(serializers.Serializer):
    asin = serializers.CharField()
    title = serializers.CharField()
    brand = serializers.CharField()
    image_small = serializers.URLField()
    image_medium = serializers.URLField()
    image_large = serializers.URLField()
    detail_page = serializers.URLField()


class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ('id', 'title', 'description', 'items', 'user')

    # id = serializers.IntegerField()
    # title = serializers.CharField()
    # description = serializers.CharField(allow_blank=True)
