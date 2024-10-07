from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app2_home'),
    path('services/', views.services, name='app2_services'),
    path('portfolio/', views.portfolio, name='app2_portfolio'),
]
