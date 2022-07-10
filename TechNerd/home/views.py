from django.shortcuts import render
from django.views import View
# Create your views here.

class HomeView(View):
    template_name = "home/home.html"
    def get(self,request):
        mylist = list(range(9))
        return render(request,self.template_name,{'list':mylist})