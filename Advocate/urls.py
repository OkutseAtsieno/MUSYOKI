from django.urls import path
from .import views

urlpatterns = [
    path('index', views.index,name='index'),
    path('Clientsection',views.Clientsection,name='Clientsection')
]


