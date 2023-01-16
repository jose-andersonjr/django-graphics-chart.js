from django.urls import re_path, path
from core import views

urlpatterns = [
    path('', views.home, name='home'),

]