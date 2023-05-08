from django.contrib import admin
from django.urls import path , include 
from . import views
from django.conf import settings
from django.conf.urls.static import static
#UrlConfiguration

app_name = 'pages'

urlpatterns = [
    
    path('Predict/', views.home, name='PredictionPage'),
    path('contact/', views.contact ,name='contact'),
    path('blog/', views.blog ,name='blog'),
    path('index/', views.index ,name='index'),
    path('', views.navbar,name='Home'),
    path('P/', views.prediction,name='Pred'),
    path('About/', views.About,name='About'),
    path('element/', views.element ,name='element'),
    
] 
