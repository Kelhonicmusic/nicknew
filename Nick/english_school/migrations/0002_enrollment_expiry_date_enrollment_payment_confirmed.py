# Generated by Django 5.1.2 on 2024-10-21 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english_school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='payment_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
