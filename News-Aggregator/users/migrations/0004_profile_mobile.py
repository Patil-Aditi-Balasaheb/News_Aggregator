# Generated by Django 3.2 on 2021-10-21 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.IntegerField(default=0),
        ),
    ]
