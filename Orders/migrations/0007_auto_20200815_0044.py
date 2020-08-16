# Generated by Django 3.0.8 on 2020-08-15 00:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0006_auto_20200812_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aorder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 15, 0, 44, 1, 997930, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='torder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 15, 0, 44, 1, 997519, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='worder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 15, 0, 44, 1, 997104, tzinfo=utc)),
        ),
    ]
