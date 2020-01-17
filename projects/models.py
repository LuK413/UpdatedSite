from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    image = models.FilePathField(
        path='/Users/kailu/Desktop/Sides/personal_website/projects/static/img')
