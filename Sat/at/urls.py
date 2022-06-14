from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('home/', views.home, name='home'),
    #path('yourname/<str:name>', views.yourname, name='yourname'),
]
