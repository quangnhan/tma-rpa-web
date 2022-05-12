from django.db import models
from django.urls import reverse

# Create your models here.

class Customer(models.Model):
    CHOICE_STATUS = [
        ('normal', "Normal"),
        ('overdue', "Overdue")
    ]
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    debt = models.FloatField()
    due_date = models.DateField()
    status = models.CharField(max_length=50, default="normal", choices=CHOICE_STATUS)
    is_reminded = models.BooleanField(default=False)

    def get_absolute_url (self):
        return reverse('customer_list')