# Generated by Django 2.0 on 2018-11-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=30)),
                ('closed', models.BooleanField(default=False)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]