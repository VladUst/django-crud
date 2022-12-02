from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import index, add_university, delete_university, edit_university, update_university, students, add_student, delete_student, edit_student, update_student

urlpatterns = [
    path('', index, name="index"),
    path('add_university', add_university, name="add_university"),
    path('delete_university/<int:id>/',
         delete_university, name="delete_university"),
    path('edit_university/<int:id>/',
         edit_university, name="edit_university"),
    path('update_university/<int:id>/',
         update_university, name="update_university"),
    path('students', students, name="students"),
    path('add_student', add_student, name="add_student"),
    path('delete_student/<int:id>/',
         delete_student, name="delete_student"),
    path('students/edit_student/<int:id>/',
         edit_student, name="edit_student"),
    path('update_student/<int:id>/',
         update_student, name="update_student"),
]
