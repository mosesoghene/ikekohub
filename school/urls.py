from django.urls import path

from school import views
from django.contrib import admin
urlpatterns = [
    path('', views.AdminDashboardView.as_view(), name='index'),
    path('admin/', admin.site.urls),
]