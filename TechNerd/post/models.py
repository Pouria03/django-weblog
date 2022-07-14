from django.db import models
from PIL import Image
# Create your models here.
from django.contrib.auth.models import User
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
    updated_date = models.DateTimeField(auto_now=True)

    def vote_count(self):
        return self.votes.count()

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


# model votes

class PostVote(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='votes')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='votes')

    def __str__(self):
        return f'{self.user} liked {self.post}'
