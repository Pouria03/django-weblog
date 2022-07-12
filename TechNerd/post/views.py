from django.shortcuts import render,get_object_or_404
from .models import Post,Category
from django.views import View
# Create your views here.

class PostListView(View):
    template_name = 'post/posts.html'
    def get(self,request):
        posts = Post.objects.all()
        return render(request,self.template_name,{'posts':posts})

class PostDetailView(View):
    template_name = 'post/detail.html'
    def get(self,request,slug):
        post = get_object_or_404(Post,slug=slug)
        tags = post.tags.split(',')
        return render(request,self.template_name,{'post':post,'tags':tags})