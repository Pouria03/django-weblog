from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from .forms import SearchForm
from .models import Post, PostVote
from django.contrib.auth.models import User

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


# processing the votes of post
class PostVoteView(View):
    def get(self,request,post_id):
        user= request.user
        post = Post.objects.get(id=post_id)
        vote = PostVote.objects.filter(user= user,post= post)
        if vote.exists():
            vote.delete()
            return redirect('post:detail',post.slug)
        elif vote.exists() == False:
            PostVote.objects.create(user= user,post= post).save()
            return redirect('post:detail',post.slug)
