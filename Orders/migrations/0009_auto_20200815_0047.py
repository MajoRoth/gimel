# Generated by Django 3.0.8 on 2020-08-15 00:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0008_auto_20200815_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aorder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 15, 0, 47, 4, 156836, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='torder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 15, 0, 47, 4, 156431, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='worder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 15, 0, 47, 4, 156025, tzinfo=utc)),
        ),
    ]
