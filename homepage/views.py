from django.shortcuts import render
 
 

from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banners.objects.all() 
    serializer_class = BannerSerializer
class SeoViewSet(viewsets.ModelViewSet):
    queryset = SEO.objects.all()
    serializer_class = SeoSerializer
    

