# Generated by Django 3.0.8 on 2020-08-16 13:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_auto_20200816_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='text_html',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 16, 13, 52, 50, 328875, tzinfo=utc)),
        ),
    ]