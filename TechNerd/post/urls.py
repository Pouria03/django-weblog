from django.urls import path
from . import views

app_name = 'post'
urlpatterns=[
    path('posts/',views.PostListView.as_view(),name='posts'),
    path('post/<slug:slug>',views.PostDetailView.as_view(),name='detail'),
]