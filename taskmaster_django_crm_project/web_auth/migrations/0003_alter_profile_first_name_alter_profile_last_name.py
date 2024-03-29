# Generated by Django 4.2.2 on 2023-08-06 08:13

import django.core.validators
from django.db import migrations, models
import taskmaster_django_crm_project.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web_auth', '0002_profile_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), taskmaster_django_crm_project.validators.validate_all_alpha, taskmaster_django_crm_project.validators.validate_first_capital]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), taskmaster_django_crm_project.validators.validate_all_alpha, taskmaster_django_crm_project.validators.validate_first_capital]),
        ),
    ]
