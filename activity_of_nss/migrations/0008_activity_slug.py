# Generated by Django 2.2.3 on 2019-09-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_of_nss', '0007_auto_20190917_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
