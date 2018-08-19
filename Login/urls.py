from django.urls import path, include
from Login.views import *
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from Login.views import (LoginView,LogoutView)


urlpatterns = [
    path('api/v1/auth/login/', LoginView.as_view()),
    path('api/v1/auth/logout/', LogoutView.as_view()),
    path('', parent_list, name='parent_list'),
    path('<int:id>/details/', parent_details, name="parent_details"),
    path('<int:id>/edit/', parent_edit, name="parent_edit"),
    path('add/', parent_add, name="parent_add"),
    path('<int:id>/delete/', parent_delete, name="parent_delete"),
    path('', teacher_list, name='teacher_list'),
    path('<int:id>/details/', teacher_details, name="teacher_details"),
    path('<int:id>/edit/', teacher_edit, name="teacher_edit"),
    path('add/', teacher_add, name="teacher_add"),
    path('<int:id>/delete/', teacher_delete, name="teacher_delete"),
]
