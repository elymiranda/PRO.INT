# Generated by Django 2.0.9 on 2018-11-21 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0013_auto_20181121_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote_date',
            field=models.DateField(verbose_name=datetime.datetime(2018, 11, 21, 16, 50, 14, 972587)),
        ),
    ]
