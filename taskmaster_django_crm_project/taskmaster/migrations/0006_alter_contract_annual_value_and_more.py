# Generated by Django 4.2.2 on 2023-08-07 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmaster', '0005_alter_contact_name_alter_contract_annual_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='annual_value',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='offer',
            name='potential_annual_value',
            field=models.FloatField(),
        ),
    ]