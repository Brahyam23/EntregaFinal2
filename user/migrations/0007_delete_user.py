# Generated by Django 4.0.6 on 2022-08-23 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_avatar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
