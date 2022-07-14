# Generated by Django 4.0.6 on 2022-07-14 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_bookings_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_id', to='home.room'),
        ),
    ]
