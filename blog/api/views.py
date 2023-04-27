from rest_framework import generics
from api import serializers
from django.contrib.auth.models import User
from api.models import Post, Comment
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import PostForm, CommentForm


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})


def login(request):
    return render(request, 'login.html')


# def create_post(request):
#     return render(request, 'create_post.html')

def create_post(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(redirect_to="/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return render(request, "create_post.html", {"form": form})


def create_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    print(request)
    if request.method == "POST":
        # form = CommentForm(request.POST)
        print(request.POST)
        comment = Comment()
        comment.body = request.POST.get("comentario")
        comment.owner = request.user
        comment.post = post
        comment.save()
        return redirect("post_detail", pk=post.id)

    return render(request, "post_detail.html", {"post": post, "comments": comments})


def post_create_view(request):
    context = {
        "form": PostForm()
    }
    if request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")
        print(title, body)
        post_object = Post.objects.create(title=title, body=body)
    return render(request, "create_post.html", context=context)


def delete_comment(request, pk):
    try:
        comentario = Comment.objects.get(id=pk)
        postId = comentario.post.id
        comentario.delete()
        return redirect("post_detail", pk=postId)
    except:
        return redirect("home")
