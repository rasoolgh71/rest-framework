from django.conf.urls import url
from . import views
from . views import UserViewSet,GroupViewSet
from rest_framework import routers
#from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    #url(r'^users/$',UserViewSet.as_view(), name='users'),
   # url(r'^groups/$',GroupViewSet.as_view(), name='groups'),
]