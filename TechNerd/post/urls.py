from django.urls import path
from . import views

app_name = 'post'
urlpatterns=[
    path('posts/',views.PostListView.as_view(),name='posts'),
    path('post/<slug:slug>',views.PostDetailView.as_view(),name='detail'),
    path('posts/<str:tag>/',views.PostsByKeywordView.as_view(),name='by_keyword'),
]