# Generated by Django 4.0.6 on 2022-07-14 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_roombooking_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roombooking',
            name='booking_date',
            field=models.DateField(default='2022-07-14'),
        ),
    ]