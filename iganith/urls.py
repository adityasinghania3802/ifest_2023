from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('base', views.base , name = "base"),
    path('start/' , views.start_quiz , name = "start"),
    path('next/<int:question_id>' , views.next_question , name="next_question"),
    path('endquiz' , views.endquiz , name= "endquiz")
]