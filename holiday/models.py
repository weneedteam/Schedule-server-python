from django.db import models

# Create your models here.
class Holiday(models.Model):
    name = models.CharField(max_length=10)
    year = models.IntegerField(max_length=4)
    month = models.IntegerField(max_length=2)
    day = models.IntegerField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)