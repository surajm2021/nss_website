# Generated by Django 2.2.3 on 2019-08-31 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='junior_student',
            name='username',
        ),
        migrations.RemoveField(
            model_name='senior_student',
            name='username',
        ),
    ]
