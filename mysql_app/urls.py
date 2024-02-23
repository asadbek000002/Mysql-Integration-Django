from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.show_data, name='show_data'),
    path('news/', views.show_data_news, name='show_data+news'),
]