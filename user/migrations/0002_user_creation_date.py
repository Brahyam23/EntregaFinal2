# Generated by Django 4.0.6 on 2022-08-06 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='creation_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
