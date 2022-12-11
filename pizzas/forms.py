from django import forms

from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_name']
        labels = {'comment_name':''}

        widgets = {'comment_name': forms.Textarea(attrs={'cols':80})}

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields = ('title', 'image')