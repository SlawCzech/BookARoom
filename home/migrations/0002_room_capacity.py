# Generated by Django 4.0.6 on 2022-07-14 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
    ]
