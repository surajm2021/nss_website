# Generated by Django 2.2.3 on 2019-09-03 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of activity', max_length=100)),
                ('description', models.TextField(help_text='Description of activity')),
                ('address', models.CharField(help_text='Address of activity', max_length=100)),
                ('date_of_activity', models.DateTimeField(default=django.utils.timezone.now)),
                ('time_of_activity', models.TimeField()),
                ('image', models.ImageField(default='default.jpeg', upload_to='Activity_pics')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
