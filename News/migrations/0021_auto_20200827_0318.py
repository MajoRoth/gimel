# Generated by Django 3.0.8 on 2020-08-27 00:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0020_auto_20200825_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 27, 0, 18, 46, 761746, tzinfo=utc)),
        ),
    ]