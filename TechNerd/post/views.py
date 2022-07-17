from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from .forms import SearchForm,CommentForm
from .models import Post, PostVote,Category,Comment
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
        title = 'all posts'
        return render(request, self.template_name, {'posts': posts,'search_form':self.form_class,'title':title})

# show details of the post:
class PostDetailView(View):
    template_name = 'post/detail.html'
    comment_Form = CommentForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post, slug=kwargs['slug'])
        self.tags = self.post_instance.tags.split(',')
        # list of comments :
        self.comments = Comment.objects.filter(post = self.post_instance)
        return super().setup(request, *args, **kwargs)

    def get(self, request,*args,**kwargs):
        form = self.comment_Form()
        return render(request, self.template_name, {'post':self.post_instance, 'tags': self.tags,'comments':self.comments,'comment_form':form})

    def post(self,request,*args,**kwargs):
        form = self.comment_Form(request.POST)
        if form.is_valid():
            comment = Comment.objects.create(user=request.user,post=self.post_instance,body=form.cleaned_data['body'])
            slug = self.post_instance.slug
        return render(request, self.template_name, {'post': self.post_instance, 'tags': self.tags,'comments':self.comments,'comment_form':self.comment_Form})


#   show posts sorted by same keyword:
class PostsByKeywordView(View):
    template_name = 'post/posts.html'

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

# show posts by category
class PostsByCategoryView(View):
    def get(self,request,slug):
        category = get_object_or_404(Category, slug=slug)
        posts = Post.objects.filter(category=category)
        return render(request,'post/posts.html',{'posts':posts,'title':slug})



