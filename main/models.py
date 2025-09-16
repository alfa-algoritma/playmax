from django.db import models
import datetime

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=255)
    thumbnail = models.URLField()
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.date.today)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    