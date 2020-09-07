from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from api import viewsets

router = DefaultRouter() 
router.register(r'book', viewsets.BookViewset)



urlpatterns = [
    path('api/', include(router.urls)),
]
