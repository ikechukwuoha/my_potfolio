from django.urls import path
from . import views

app_name = 'ikechukwu'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('education/', views.education, name = 'education'),
    path('experience/', views.experience, name = 'experience'),
    path('portolio/', views.portfolio, name = 'portfolio'),
    path('service/', views.service, name = 'service'),
]