from django.shortcuts import render
from django.views import View
from post.models import Post,Category
from .models import About
# Create your views here.

class HomeView(View):
    template_name = "home/home.html"
    def get(self,request):
        posts = Post.objects.all()[:5]
        return render(request,self.template_name,{'posts':posts})


# about us view:
class AboutView(View):
    def get(self,request):
        data = About.objects.first()
        return render(request,'home/about.html',{'data':data})