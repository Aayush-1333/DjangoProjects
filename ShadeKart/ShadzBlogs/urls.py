from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blogIndex'),
    path('blogPosts', views.blogPost, name='blogPosts'),
    path('about', views.about, name='about'),
    path('search', views.search, name='SearchResults'),
    path('submitPost', views.submitPost, name='SubmitPost'),
    path('officialPost1', views.officialPost1, name='Official 1'),
    path('officialPost2', views.officialPost2, name='Official 2'),
    path('postView<int:postId>', views.postView, name='PostView')
]
