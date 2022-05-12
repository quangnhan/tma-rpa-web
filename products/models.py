from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    code = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50)
    unit_price = models.FloatField()
    total_amount = models.FloatField()

    def get_absolute_url (self):
        return reverse('product_detail', args=[str(self.id)])

#Signals
@receiver(post_save, sender=Product)
def post_save_create_or_update_product(sender, instance, created, **kwargs):
    if created:
        pass