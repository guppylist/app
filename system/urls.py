from django.conf.urls import url, include

from rest_framework import routers

from system import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'search/products', views.ApiProductSearchViewSet, base_name='search_products')
router.register(r'products', views.ApiProductViewSet, base_name='products')
router.register(r'lists', views.ApiListViewSet, base_name='lists')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]