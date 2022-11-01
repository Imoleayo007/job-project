from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from myapp.models import JobAdvert, JobApplication

class JobAdvert_Serializer(serializers.ModelSerializer):
    job_application_count = serializers.ReadOnlyField()

    class Meta:
        model = JobAdvert
        fields = '__all__'

        
class JobApplication_Serializer(serializers.ModelSerializer):
    job_advert_count = serializers.ReadOnlyField()

    class Meta:
        model = JobApplication
        fields = '__all__'

