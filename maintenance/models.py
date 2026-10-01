from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class MaintenanceRequest(models.Model):
    CATEGORY = [
        ('Electrical', 'Electrical'),
        ('Plumbing', 'Plumbing'),
        ('Climbing', 'Climbing'),
        ('Furniture', 'Furniture'),
        ('Other', 'Other'),
    ]


    PRIORITY = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ]

    STATUS = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length= 100)
    description = models.TextField()
    category = models.CharField(max_length= 20, choices = CATEGORY)
    priority = models.CharField(max_length= 20, choices = PRIORITY)
    status = models.CharField(max_length= 20, choices = STATUS)
    location = models.CharField(max_length= 100)
    date_Reported = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.title


