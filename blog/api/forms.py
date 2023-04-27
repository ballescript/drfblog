from django import forms


class PostForm(forms.Form):
    title = forms.CharField(label="Post title", max_length=100)
    content = forms.CharField(label="Post content", widget=forms.Textarea)
