# Generated by Django 2.2 on 2019-04-30 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0021_auto_20190430_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 30, 10, 51, 21, 745540)),
        ),
    ]
