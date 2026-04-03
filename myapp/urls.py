from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_student),
    path('delete/<int:id>/', views.delete_student),
    path('update/<int:id>/', views.update_student),
]