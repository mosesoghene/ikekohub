from django.urls import path

from school import views

urlpatterns = [
    path('', views.index, name='index'),
]