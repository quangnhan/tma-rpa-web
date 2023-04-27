from django.db import models

# Create your models here.

class Invoice(models.Model):
    invoice_no = models.CharField(max_length=255)
    serial = models.CharField(max_length=255)
    po_contract_no = models.CharField(max_length=255)
    currency_code = models.CharField(max_length=255)
    vat_code = models.CharField(max_length=255)
    pretax_amt = models.FloatField(max_length=255)
    vat_amt = models.FloatField(max_length=255)
    total_amt = models.FloatField(max_length=255)
