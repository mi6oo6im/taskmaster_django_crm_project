from django.core import validators
from django.db import models
from taskmaster_django_crm_project.utilities import TimestampMixin, ChoicesMixin


class Industry(ChoicesMixin):
    EDUCATION = 'Education'
    TECHNOLOGY = 'Technology'
    HEALTHCARE = 'Healthcare'
    FINANCE = 'Finance'
    RETAIL = 'Retail'
    OTHER = 'Other'


class Organization(TimestampMixin, models.Model):
    name = models.CharField(
        max_length=100,
        validators=(
            validators.MinLengthValidator(2),
        )
    )
    address = models.TextField(
        null=True,
        blank=True,
    )
    contact_number = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )
    industry = models.CharField(
        max_length=Industry.max_length(),
        null=True,
        blank=True,
        choices=Industry.choices(),
    )

    def __str__(self):
        return self.name


class Customer(TimestampMixin, models.Model):
    sales_representative = models.ManyToManyField('web_auth.Profile')
    name = models.CharField(
        max_length=100
    )
    address = models.TextField(
        null=True,
        blank=True,
    )
    industry = models.CharField(
        max_length=Industry.max_length(),
        null=True,
        blank=True,
        choices=Industry.choices(),
    )

    def __str__(self):
        return self.name


class Contact(TimestampMixin, models.Model):
    company = models.ForeignKey(
        null=True,
        blank=True,
        to=Customer,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(2),
        )
    )
    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )
    contact_number = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Task(TimestampMixin, models.Model):
    company = models.ForeignKey(
        to=Customer,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=200,
    )
    due_date = models.DateField(
        null=True,
        blank=True,
    )
    completed = models.BooleanField(
        default=False,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class Offer(TimestampMixin, models.Model):
    company = models.ForeignKey(
        to=Customer,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=200,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    valid_until = models.DateField()
    potential_annual_value = models.FloatField()

    def __str__(self):
        return self.title


class Contract(TimestampMixin, models.Model):
    company = models.ForeignKey(
        to=Customer,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=200,
    )
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    annual_value = models.FloatField()

    def __str__(self):
        return self.title
