from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path , include  
from .views import *
router = DefaultRouter()
router.register(r'banners',BannerViewSet , "BannerHomePage")
router.register(r'seo',SeoViewSet , "seo")
urlpatterns = [
    path('' , include(router.urls))
]
