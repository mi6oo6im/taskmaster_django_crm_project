# Generated by Django 4.2.2 on 2023-07-09 07:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import taskmaster_django_crm_project.web_auth.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', taskmaster_django_crm_project.web_auth.models.AppUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_picture/')),
                ('job_title', models.CharField(blank=True, choices=[('MANAGER', 'Manager'), ('SALES_ASSOCIATE', 'Sales Associate'), ('MARKETING_SPECIALIST', 'Marketing Specialist'), ('ENGINEER', 'Engineer'), ('OTHER', 'Other')], max_length=20, null=True)),
                ('department', models.CharField(blank=True, choices=[('SALES', 'Sales'), ('MARKETING', 'Marketing'), ('ENGINEERING', 'Engineering'), ('HR', 'Human Resources'), ('OTHER', 'Other')], max_length=15, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
