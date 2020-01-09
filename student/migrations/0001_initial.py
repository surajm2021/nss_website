# Generated by Django 2.2.3 on 2019-08-31 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Branch_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender_list', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='status_of_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status_list', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='senior_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Mobile_no', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=100)),
                ('Branch', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.branch')),
                ('Sex', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.gender')),
                ('Status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.status_of_student')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='junior_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Mobile_no', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=100)),
                ('Branch', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.branch')),
                ('Sex', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.gender')),
                ('Status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.status_of_student')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
