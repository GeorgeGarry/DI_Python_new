# Generated by Django 4.2.4 on 2023-08-27 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_post_released_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='released_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 27, 16, 48, 18, 330409)),
        ),
    ]