from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.CharField(max_length=400)

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.CharField(max_length=400)
    body = models.TextField()
    image = models.ImageField(blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,related_name='category_posts')
    tags = models.CharField(max_length=100)