#rest framework viewsets and mixins 
from rest_framework import viewsets, mixins

#import models 
from api.models import Book

#import serializers
from api.serializers import BookSerializer


class BookViewset(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    ''' lookup_field="title" '''
