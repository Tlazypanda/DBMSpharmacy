# Generated by Django 2.2 on 2019-04-29 00:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0011_auto_20190427_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 29, 0, 10, 7, 292550)),
        ),
    ]
