from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import SearchForm
from .models import Post


# Create your views here.

class PostListView(View):
    template_name = 'post/posts.html'
    form_class = SearchForm
    def get(self, request):
        posts = Post.objects.all()
        if request.GET.get('search'):
            posts = posts.filter(title__contains=request.GET['search']) or\
                    posts.filter(body__contains=request.GET['search'])
        return render(request, self.template_name, {'posts': posts,'search_form':self.form_class})


class PostDetailView(View):
    template_name = 'post/detail.html'

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        tags = post.tags.split(',')
        return render(request, self.template_name, {'post': post, 'tags': tags})


#   show posts sorted by same keyword:
class PostsByKeywordView(View):
    template_name = 'post/search_by_keywords.html'

    def get(self, request, tag):
        posts = Post.objects.filter(tags__contains=tag)
        title = f'posts related to {tag}'
        return render(request, self.template_name, {'posts': posts, 'title': title})
