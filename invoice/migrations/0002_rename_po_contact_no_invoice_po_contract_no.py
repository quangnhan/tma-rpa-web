# Generated by Django 4.1.7 on 2023-04-27 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='po_contact_no',
            new_name='po_contract_no',
        ),
    ]