# rest framework
from rest_framework import serializers

#import models
from api.models import Book

class BookSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Book
        fields = '__all__'