from django.urls import  path
from . import views
app_name = 'main'

urlpatterns = [
    path('',views.BaseView.as_view(), name='base'),
    path('home/',views.HomeView.as_view(), name='home'),
    path('login/',views.LogInView.as_view(), name='login'),
    path('logout/',views.log_out, name='logout'),
    path('register/',views.SignUp.as_view(),name='register'),
    path('user-home/',views.SuggestionJobView.as_view(),name='user_home'),
    path('result/',views.ResultView.as_view(),name='result'),
]
