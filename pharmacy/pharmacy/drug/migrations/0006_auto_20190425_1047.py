# Generated by Django 2.2 on 2019-04-25 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0005_auto_20190425_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 25, 10, 46, 59, 734420)),
        ),
    ]
