from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class About(models.Model):
     title = models.CharField(max_length=150)
     body = RichTextUploadingField()

     def __str__(self):
          return self.title