from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from system.serializers import UserSerializer, GroupSerializer, ProductSerializer
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
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        """
        Product search.

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        q = request.GET.get('q')
        results = AmazonApi.search(q)

        serializer = ProductSerializer(instance=results, many=True)
        return Response(serializer.data)


class ApiProductViewSet(viewsets.ViewSet):
    """
    API endpoints for product data via the Amazon API.
    """
    serializer_class = ProductSerializer

    def retrieve(self, request, pk=None):
        """
        Product details

        [GET] /api/products/{pk}

        :param request:
        :param pk:
        :return:
        """
        results = AmazonApi.get_product_details(pk)
        serializer = ProductSerializer(instance=results)

        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        """
        Product list.

        [GET] /api/products/

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return Response({'test': 'foo'})

    @detail_route(methods=['get'])
    def similar(self, request, *args, **kwargs):
        """
        Similar products list.

        [GET] /api/products/{pk}/similar

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        asin = kwargs['pk']
        results = AmazonApi.get_similar_products(asin)
        serializer = ProductSerializer(instance=results, many=True)

        return Response(serializer.data)