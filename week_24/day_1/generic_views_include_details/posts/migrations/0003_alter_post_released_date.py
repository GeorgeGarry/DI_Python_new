# Generated by Django 4.2.4 on 2023-09-07 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_released_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='released_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 7, 16, 56, 22, 342380)),
        ),
    ]
