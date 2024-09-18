from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_std, name='add_std'),
    path('form/', views.form, name='form'),
    path('display/', views.display_student, name='display_student'),
    path('delete/', views.delete_student, name='delete_student'),
    path('edit/', views.edit_student, name='edit_student'),
    path('update/', views.update_student, name='update_student'),
]
