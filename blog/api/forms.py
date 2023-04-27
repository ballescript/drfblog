from django import forms


class PostForm(forms.Form):
    title = forms.CharField(label="Post title", max_length=100)
    body = forms.CharField(label="Post body", widget=forms.Textarea)


class CommentForm(forms.Form):
    body = forms.CharField(label="Comment body", widget=forms.Textarea)
