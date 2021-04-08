from django.db import models


class ImgModel(models.Model):
    img = models.ImageField()


class Story(models.Model):
    images = models.ManyToManyField(ImgModel)