'''
Created on 2018. 11. 4.

@author: user
'''
from django.forms.models import ModelForm
from .models import Post
from django import forms
class PostForm(ModelForm):
    
    files = forms.FileField(required=False, 
                            widget=forms.ClearableFileInput(attrs={'multiple':True}))
    images = forms.ImageField(required=False,
                              widget=forms.ClearableFileInput(attrs={'multiple':True}))
    class Meta:
        model = Post
        fields=['type', 'headline', 'content']
        
        
        
        
        
        