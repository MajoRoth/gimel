# Generated by Django 3.0.8 on 2020-08-16 09:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_auto_20200816_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 16, 9, 11, 14, 873614, tzinfo=utc)),
        ),
    ]
