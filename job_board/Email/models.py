
from django.db import models

class JobListing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    is_new = models.BooleanField(default=True) 

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=100)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.applicant_name} - {self.job.title} - {self.status}"



