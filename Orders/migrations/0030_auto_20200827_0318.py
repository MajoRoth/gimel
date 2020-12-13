# Generated by Django 3.0.8 on 2020-08-27 00:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0029_auto_20200825_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='worder',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aorder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 27, 0, 18, 46, 748526, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='torder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 27, 0, 18, 46, 747600, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='worder',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 27, 0, 18, 46, 746681, tzinfo=utc)),
        ),
    ]