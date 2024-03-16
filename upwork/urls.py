from django.urls import path
from upwork import views

urlpatterns = [
    path('', views.home, name='home'),
    path('file/', views.upload_file, name='file'),
    path('text/', views.text_file, name='text'),
    path('task2/', views.chart_file, name='task2'),
]
