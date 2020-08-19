# Generated by Django 3.0.8 on 2020-08-16 08:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0009_auto_20200815_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aorder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 16, 8, 58, 39, 243694, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='torder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 16, 8, 58, 39, 243129, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='worder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 16, 8, 58, 39, 242391, tzinfo=utc)),
        ),
    ]