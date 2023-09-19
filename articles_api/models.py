from django.db import models

# Create your models here.

class Article(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)
    reading_time = models.FloatField()
    summary = models.CharField(max_length=1000)
    notes = models.CharField(max_length=2000)
    related_links = models.CharField(max_length=100)
