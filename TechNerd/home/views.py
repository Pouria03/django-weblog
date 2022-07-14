from django.shortcuts import render
from django.views import View
from post.models import Post,Category
# Create your views here.

class HomeView(View):
    template_name = "home/home.html"
    def get(self,request):
        posts = Post.objects.all()[:5]
        return render(request,self.template_name,{'posts':posts})