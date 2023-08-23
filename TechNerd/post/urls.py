from django.urls import path
from . import views

app_name = 'post'
urlpatterns=[
    path('posts/',views.PostListView.as_view(),name='posts'),
    path('post/<slug:slug>/',views.PostDetailView.as_view(),name='detail'),
    path('posts/<str:tag>/',views.PostsByKeywordView.as_view(),name='by_keyword'),
    path('post/vote/<int:post_id>/',views.PostVoteView.as_view(),name='vote'),
    path('posts/category/<slug:slug>/',views.PostsByCategoryView.as_view(),name='by_category'),
    path('favorites/',views.PostFavoriteView.as_view(),name='favorite_posts')
]
