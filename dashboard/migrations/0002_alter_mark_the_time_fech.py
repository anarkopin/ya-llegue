# Generated by Django 3.2.8 on 2021-11-26 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark_the_time',
            name='fech',
            field=models.DateField(default=datetime.date(2021, 11, 26)),
        ),
    ]
