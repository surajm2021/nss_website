# Generated by Django 2.2.3 on 2019-09-07 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_branch_gender_nss_team_member_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nss_team_member',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='nss_team_member',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='nss_team_member',
            name='status',
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='Nss_team_member',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]