from django.shortcuts import render,redirect
from django.views.generic import TemplateView,DetailView,DeleteView,UpdateView
from movie.forms import AddMovieForm,EditMovieForm
from django.views import View
from movie.models import Movie
from django.urls import reverse_lazy


class HomeView(View):
    def get(self,request):
        m = Movie.objects.all()
        return render(request,'home.html',{'movie':m})

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'
    pk_url_kwarg = 'id'


class MovieDelete(DeleteView):
    model = Movie
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('movie:HomeView')
    template_name = 'movie_confirm_delete.html'


class MovieEditView(UpdateView):
    model = Movie
    form_class = EditMovieForm
    template_name = 'edit_movie.html'
    success_url = reverse_lazy('movie:HomeView')
    pk_url_kwarg = 'id'


class AddMovie(View):
    def get(self,request):
        form = AddMovieForm()
        return render(request,'add_movie.html',{'form':form})

    def post(self,request):
        if (request.method == 'POST'):
            name = request.POST.get('name')
            image = request.FILES.get("image")
            lang = request.POST.get('language')
            det = request.POST.get('details')

            c = Movie.objects.create(name=name, image=image, language=lang, details=det)
            c.save()
            return redirect('movie:HomeView')

