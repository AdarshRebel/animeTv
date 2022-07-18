from django.urls import path
from animeTv import views

urlspatterns = [
    path('', views.show_animeTv),
    path('new', views.show_new),
]
