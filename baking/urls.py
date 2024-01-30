from django.urls import path
from .import views

#URL conf
urlpatterns = [
    path('', views.welcome),
    path('index/', views.index)
    
]