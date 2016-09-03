from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework.response import Response

from system.serializers import UserSerializer, GroupSerializer, ProductSearchSerializer
from core.amazon.api import AmazonApi


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ApiProductSearchViewSet(viewsets.ViewSet):
    """
    API endpoint for product search.

    @see https://medium.com/django-rest-framework/django-rest-framework-viewset-when-you-don-t-have-a-model-335a0490ba6f#.mze73umct
    """
    serializer_class = ProductSearchSerializer

    def list(self, request, *args, **kwargs):
        q = 'kindle paperwhite'
        results = AmazonApi.search(q)

        serializer = ProductSearchSerializer(instance=results, many=True)
        return Response(serializer.data)
