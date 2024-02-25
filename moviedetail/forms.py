from django import forms
from .models import Movie, Review
from django.contrib.auth.models import User


class MdetailForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['user','movie_title','poster','desc','release_date','actors','category','youtube_link']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']