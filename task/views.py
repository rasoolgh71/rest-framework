from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import serializers,viewsets
from .serializer import UserSerializer,GroupSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow user
    """
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow group
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def home(request):
    return render(request,'task/base.html')