# Generated by Django 2.0.9 on 2018-11-21 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0010_auto_20181121_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 11, 21, 18, 47, 45, 301271)),
        ),
    ]
