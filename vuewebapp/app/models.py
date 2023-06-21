from django.db import models

# Create your models here.
class Posts(models.Model):

    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Tests(models.Model):

    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title
  
class Image(models.Model):
    image = models.ImageField()

class ImageNew(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField()

    def __str__(self):
        return self.title
  