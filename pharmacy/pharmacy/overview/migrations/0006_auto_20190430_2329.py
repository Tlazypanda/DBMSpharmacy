# Generated by Django 2.2 on 2019-04-30 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0005_auto_20190430_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.BigIntegerField(default=1234567890),
        ),
    ]
