# Generated by Django 3.0.8 on 2020-08-25 12:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0017_auto_20200825_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 25, 12, 41, 4, 140164, tzinfo=utc)),
        ),
    ]
