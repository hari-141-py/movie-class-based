"""
URL configuration for Movie_Class project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'movie'

urlpatterns = [
    path('',views.HomeView.as_view(),name="HomeView"),
    path('AddMovie',views.AddMovie.as_view(),name="AddMovie"),
    path('MovieEditView/<int:id>',views.MovieEditView.as_view(),name="MovieEditView"),
    path('MovieDetailView/<int:id>',views.MovieDetailView.as_view(),name="MovieDetailView"),
    path('MovieDelete/<int:id>',views.MovieDelete.as_view(),name="MovieDelete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)