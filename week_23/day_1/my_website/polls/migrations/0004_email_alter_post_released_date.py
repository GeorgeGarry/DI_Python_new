# Generated by Django 4.2.4 on 2023-08-27 17:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('polls', '0003_alter_post_released_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.person')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='released_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 27, 17, 12, 8, 698856)),
        ),
    ]