from django.contrib.auth.hashers import make_password
from django.core import validators
from django.db import models
from django.contrib.auth import get_user_model, models as auth_models
from taskmaster_django_crm_project.utilities import TimestampMixin, ChoicesMixin


# Create your models here.

class AppUserManager(auth_models.BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given username must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class AppUser(auth_models.PermissionsMixin, auth_models.AbstractBaseUser, TimestampMixin):
    USERNAME_FIELD = 'email'

    objects = AppUserManager()

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )


UserModel = get_user_model()


class JobTitle(ChoicesMixin):
    MANAGER = 'Manager'
    SALES_ASSOCIATE = 'Sales Associate'
    MARKETING_SPECIALIST = 'Marketing Specialist'
    ENGINEER = 'Engineer'
    OTHER = 'Other'


class Department(ChoicesMixin):
    SALES = 'Sales'
    MARKETING = 'Marketing'
    ENGINEERING = 'Engineering'
    HR = 'Human Resources'
    OTHER = 'Other'


# TODO finalize Profile model and make migrations
class Profile(TimestampMixin, models.Model):
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(2),
        )
    )
    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(2),
        )
    )

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    profile_picture = models.ImageField(
        upload_to='profile_picture/',
        null=True,
        blank=True,
    )
    job_title = models.CharField(
        max_length=JobTitle.max_length(),
        null=True,
        blank=True,
        choices=JobTitle.choices(),
    )
    department = models.CharField(
        max_length=Department.max_length(),
        null=True,
        blank=True,
        choices=Department.choices(),
    )

    def __str__(self):
        return self.full_name
