# Generated by Django 3.1.1 on 2022-05-12 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debt_reminder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='is_overdued',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='is_reminded',
            field=models.BooleanField(default=False),
        ),
    ]
