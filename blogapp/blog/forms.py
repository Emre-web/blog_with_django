from django import forms
from .models import Comment, Post #models.py dosyasındaki Comment ve Post modellerini import ettik

class PostForm(forms.ModelForm): #PostForm adında bir class oluşturduk ve forms.ModelForm sınıfından miras aldık
    class Meta:
        model = Post #modelin adının post oldğunu belirttik
        fields = ['title', 'content'] #modeldeki alanları belirttik
        #fields = '__all__' #tüm alanları almak için bu şekilde de belirtebiliriz

#şimdi de comment formunu oluşturalım
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'postcomment'] #modeldeki alanları belirttik
        #fields = '__all__' #tüm alanları almak için bu şekilde de belirtebiliriz