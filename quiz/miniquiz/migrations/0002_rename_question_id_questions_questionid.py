# Generated by Django 4.0.3 on 2022-04-05 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniquiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='question_id',
            new_name='questionid',
        ),
    ]