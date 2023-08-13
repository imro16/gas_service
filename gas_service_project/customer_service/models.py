from django.db import models
from django.utils import timezone

class Customer(models.Model):
    first_name = models.TextField(null=True, default='Default first name')
    last_name = models.TextField(null=True, default='Default ast name')
    email = models.EmailField(unique=True, null=True, default='example@example.com')
    phone_number = models.CharField(max_length=20)
    address = models.TextField(null=True, default='Default Address')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100, null=True, default='Default Request Type')
    request_details = models.TextField()
    attached_file = models.FileField(upload_to='service_request_files/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    submitted_date = models.DateTimeField(default=timezone.now)
    resolved_date = models.DateTimeField(default=timezone.now)
    details = models.TextField(max_length=100, null=True, default='Default Request Type')
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)

    def __str__(self):
        return f'{self.request_type} - {self.customer}'

