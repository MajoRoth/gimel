# Generated by Django 3.0.8 on 2020-08-15 00:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0007_auto_20200815_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aorder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 15, 0, 45, 48, 439564, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='torder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 15, 0, 45, 48, 438935, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='worder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 15, 0, 45, 48, 438237, tzinfo=utc)),
        ),
    ]
