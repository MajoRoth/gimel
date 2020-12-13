# Generated by Django 3.0.8 on 2020-08-25 12:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0025_auto_20200825_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aorder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 25, 12, 40, 54, 918268, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='torder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 25, 12, 40, 54, 917664, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='worder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 25, 12, 40, 54, 917194, tzinfo=utc)),
        ),
    ]