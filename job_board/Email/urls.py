from django.urls import path
from . import views

urlpatterns = [
    path('new-job-notification/', views.send_new_job_notification, name='new-job-notification'),
    path('application-status-update/', views.send_application_status_update, name='application-status-update'),
]
