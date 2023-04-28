from django import forms
from .models import Post, Comment


# class PostForm(forms.Form):
#     title = forms.CharField(label="Post title", max_length=100)
#     body = forms.CharField(label="Post body", widget=forms.Textarea)

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title", "body")



# class CommentForm(forms.Form):
#     body = forms.CharField(label="Comment body", widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("body",)
        labels = {
            "body": "Comment"
        }

