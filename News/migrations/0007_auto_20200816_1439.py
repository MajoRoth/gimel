# Generated by Django 3.0.8 on 2020-08-16 14:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0006_auto_20200816_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 16, 14, 39, 3, 925152, tzinfo=utc)),
        ),
    ]
