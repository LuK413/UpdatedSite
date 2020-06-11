from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    previewDescription = models.CharField(max_length=300, default='preview')
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    image = models.ImageField()
    link = models.URLField(default='http://127.0.0.1:8000/')
