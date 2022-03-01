from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('', views.BaseView.as_view(), name='base'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.SignUp.as_view(), name='register'),
    path('user-home/', views.SuggestionJobView.as_view(), name='user_home'),
    path('result/', views.ResultView.as_view(), name='result'),
    path('profilepage/', views.UserProfileView.as_view(), name='profile'),
    path('profilepage/experience/<int:pk>', views.ExperienceDetailView.as_view(), name='detail'),
    path('create/', views.ExperienceCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.ExperienceUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.ExperienceDeleteView.as_view(), name='delete'),
    path('success/',views.SuccessView.as_view(),name='success'),
    path('user-home/job/<int:pk>', views.JobDetailView.as_view(), name='job_detail'),
    path('addjob/', views.JobCreateView.as_view(), name='add_job'),
    path('updatejob/<int:pk>', views.JobUpdateView.as_view(), name='update_job'),
    path('deletejob/<int:pk>', views.JobDeleteView.as_view(), name='delete_job'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)