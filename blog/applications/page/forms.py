from django import forms
from .models import PageModel
from ckeditor_uploader.fields import RichTextUploadingField

class PageForm(forms.ModelForm):

    class Meta:
        model = PageModel
        fields = ['title', 'content', 'resume']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'resume': forms.Textarea(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }
        labels = {
            'title':'', 'resume': '', 'content': ''
        }