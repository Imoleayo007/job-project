import email
from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



# Create your models here.

EMPLOYMENT_TYPE = (
    ('FULL_TIME', 'Full-time'),
    ('PART_TIME', 'Part-time'),
    ('REMOTE', 'Remote'),
    ('CONTRACT', 'Contract')
)
EXPERIENCE_LEVEL = (
    ('ENTRY_LEVEL', 'Entry_level'),
    ('MID_LEVEL', 'Mid-level'),
    ('SENIOR_LEVEL', 'Senior-level')
)
STATUS = (
    ("UNPUBLISHED","Unpublished"), 
    ("PUBLISHED","Published")
)

class JobAdvert(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=150)
    employment_type = models.CharField(choices=EMPLOYMENT_TYPE, max_length=150)
    experience_level = models.CharField(choices=EXPERIENCE_LEVEL, max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=100)
    job_description = models.TextField()
    status = models.CharField(choices=STATUS, max_length=100, default= 'PUBLISHED')
    date_posted = models.DateField(auto_now= True)

    def __str__(self):
        return f"{self.title} ---- {self.company_name}"



EXPERIENCE_LEVEL = (("0 - 1", "0 - 1"), 
                         ("1 - 2", "1 - 2"), 
                         ("3 - 4", "3 - 4"),
                         ("5 - 6", "5 - 6"), 
                         ("7 and above", "7 and above")
                        )

class JobApplication(models.Model):
    Job_Advert = models.ForeignKey(JobAdvert, related_name="Job_application", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email_address = models.EmailField()
    linkedin_profile_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    years_of_experience = models.CharField(max_length=50, choices= EXPERIENCE_LEVEL)
    upload_cv = models.FileField(upload_to='static/myapp', null=True)
    cover_letter = models.TextField(null=True, blank=True)
    time_and_date_applied = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Application for --- {self.Job_Advert}"

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



