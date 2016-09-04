from django.contrib.auth.models import User, Group
from rest_framework import serializers


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
