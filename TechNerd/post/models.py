from django.db import models
from PIL import Image

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.slug

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.CharField(max_length=400)
    body = models.TextField()
    image = models.ImageField(default=None,blank=True)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,related_name='category_posts')
    tags = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ['-created_date']

    def __str__(self):
        return self.slug

    def save(self):
        super().save()
        if self.image:
            img = Image.open(self.image.path)
            img.thumbnail((200,200))
            img.save(self.image.path)

