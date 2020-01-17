from django.db import models


class About(models.Model):
  description = models.TextField()
  image = models.FilePathField(
      path='/Users/kailu/Desktop/Sides/personal_website/about/static/img')
