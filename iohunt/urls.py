from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('<int:Round>', views.iohome, name='iohome'),
    path('ended/<int:Round>', views.ended, name='ended'),
    path('<int:Round>/<slug:slug>', views.puzzle, name='puzzle'),
]