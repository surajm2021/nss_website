# Generated by Django 2.2.3 on 2019-09-07 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_branch_gender_nss_team_member_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='nss_team_member',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
