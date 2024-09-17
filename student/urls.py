from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_std, name='add_std'),  # Corrected `view` to `views`
    path('detail/', views.display, name='display'),  # Corrected `view` to `views`
    path('form/', views.form, name='form'),  # Corrected `view` to `views`
]
