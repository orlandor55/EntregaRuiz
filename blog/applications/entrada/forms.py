from django import forms
from .models import Entry


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['title', 'content', 'resume', 'sub_title', 'category', 'tag', 'public', 'portada', 'in_home']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'sub_title title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subtítulo'}),
            'resume': forms.Textarea(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
            'tag': forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
            'public': forms.CheckboxInput(attrs={'class':'form-control'}),
            'public': forms.CheckboxInput(attrs={'class':'form-control'}),
            'in_home': forms.CheckboxInput(attrs={'class':'form-control'}),
        }
        labels = {
            'title':'', 
            'sub_title':'', 
            'resume': '', 
            'content': '', 
            'category': '', 
            'tag': '', 
            'public': '', 
            'portada': '', 
            'in_home': ''
        }