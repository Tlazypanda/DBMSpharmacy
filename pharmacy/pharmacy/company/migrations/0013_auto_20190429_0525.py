# Generated by Django 2.2 on 2019-04-29 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_order_fulfilled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='fulfilled',
        ),
        migrations.AddField(
            model_name='userorder',
            name='fulfilled',
            field=models.BooleanField(default=False),
        ),
    ]