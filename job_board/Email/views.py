from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import JobListing, JobApplication
from django.conf import settings
from users.models import User

def send_new_job_notification(request):
    # Retrieve new job listings that haven't been notified yet
    new_job_listings = JobListing.objects.filter(is_new=True)

    # Retrieve users who want to receive email notifications
    users = User.objects.filter(is_applicant=True)

    for user in users:
        # Retrieve the user's email
        recipient = user.email

        # Prepare a list of new job listings for this user
        user_job_listings = [job_listing for job_listing in new_job_listings]

        # Prepare the email subject and message
        subject = 'New Job Listings Notification'
        message = render_to_string('email/new_job_notification.html', {'user': user, 'job_listings': user_job_listings})

        # Send the email
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])

    # Mark all new job listings as notified
    new_job_listings.update(is_new=False)

    return HttpResponse("New job notification emails sent successfully!")

def send_application_status_update(request):
    # Retrieve updated job applications
    updated_applications = JobApplication.objects.filter(status=True)
    
    for application in updated_applications:
        # Retrieve the applicant's email
        recipient = application.applicant.email

        # Prepare the email subject and message
        subject = f'Application Status Update: {application.job_title}'
        message = render_to_string('email/application_status_update.html', {'application': application})

        # Send the email
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])

        # Reset the status_updated flag
        application.status_updated = False
        application.save()

    return HttpResponse("Application status update notification emails sent successfully!")
