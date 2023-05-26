from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('software_developer/', views.software_developer, name='software_developer'),
]