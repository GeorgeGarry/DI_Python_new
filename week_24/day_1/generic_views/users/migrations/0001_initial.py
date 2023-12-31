# Generated by Django 4.2.4 on 2023-09-07 15:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('birth_date', models.DateField()),
                ('has_pet', models.BooleanField(default=True)),
                ('number_pet', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
            ],
        ),
    ]
