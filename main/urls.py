
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about,name='about'),
    path('trophy',views.trophy,name='trophy'),
    path('create',views.create,name='create'),


]
