from django.db import models

# Create your models here.
class Job(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=30)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    duties = models.CharField(max_length=200)