# Generated by Django 2.2.3 on 2019-09-16 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_of_nss', '0005_auto_20190916_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='activity',
        ),
    ]
