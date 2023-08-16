from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# ==========================================================================================================
# this is Category Table :
class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.slug
# End =====================================================================================================

# this is Post Table :
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.CharField(max_length=400)
    body = RichTextUploadingField()
    image = models.ImageField(upload_to='products/%Y/%m/%d/',default=None,blank=True)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,related_name='category_posts')
    # tags should divide by comma ','
    tags = models.CharField(max_length=100,verbose_name='tags (tags must be divided by comma)')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def vote_count(self):
        return self.votes.count()

    class Meta():
        ordering = ['-created_date']

    def __str__(self):
        return self.slug


# End =======================================================================================================

# this is for Votes :
class PostVote(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='votes')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='votes')

    def __str__(self):
        return f'{self.user} liked {self.post}'

# End =======================================================================================================

# this is comment table :
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='comments')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField(max_length=500)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' \'{self.user.username}\' commented for \'{self.post.title}\' '

    class Meta:
        ordering = ('-comment_date',)
# End =======================================================================================================
