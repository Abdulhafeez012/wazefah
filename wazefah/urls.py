from django.urls import  path
from . import views

app_name = 'wazefah'

urlpatterns = [
    path('',views.BaseView.as_view(), name='base'),
    path('home/',views.HomeView.as_view(), name='home'),
    path('logIn/',views.LogInView.as_view(), name='login'),
    path('logout/',views.log_out, name='logout'),
    path('register/',views.SignUp.as_view(),name='register'),
]