# Generated by Django 2.2.3 on 2019-09-06 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_of_nss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=models.ImageField(upload_to='Activity_pics'),
        ),
    ]
