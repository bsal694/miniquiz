# Generated by Django 4.0.3 on 2022-05-18 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_tempprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempprofile',
            name='otpSessionID',
        ),
    ]