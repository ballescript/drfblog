from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from .views import home, post_detail, login, create_post, create_comment, delete_comment

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', create_comment, name='create_comment'),
    path('', home, name='home'),
    # path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<int:pk>/', create_comment, name='post_detail'),
    path('login/', login, name='login'),
    path('create-post', create_post, name='create_post'),
    path('delete-comment/<int:pk>/', delete_comment, name="delete_comment")
]

urlpatterns = format_suffix_patterns(urlpatterns)
