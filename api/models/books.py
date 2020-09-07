from django.db import models

# model libro 

class Book(models.Model):
    title = models.CharField(max_length=20)
    descriptions =models.TextField()

    def __str__(self):
        return self.title