from django import forms
from movie.models import Movie

class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name','image','language','details']

class EditMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name','image','language','details']
