from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    
    path("",views.fun,name="myapp"),
    path("generate/",views.fun,name ="myapp"),
    path("favicon.ico/HTTP/1.1",views.fun,name ="myapp")
]