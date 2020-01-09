# Generated by Django 2.2.3 on 2019-09-07 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20190907_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Nss_team_member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of nss team memner', max_length=100)),
                ('batch', models.CharField(max_length=100)),
                ('achievement', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='nss_team_member_pics')),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Status')),
                ('sex', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Gender')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Branch')),
            ],
        ),
    ]
