# Generated by Django 4.0.6 on 2022-07-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_roombooking_delete_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roombooking',
            name='booking_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]