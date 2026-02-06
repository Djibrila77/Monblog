from django.urls import path
from .import views
app_name='blog_app'


urlpatterns =[
   path('', views.home_view, name='home'),
   path('confirmation/', views.confirmation_view, name='confirmation'),
]
