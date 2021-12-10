# Generated by Django 3.2.9 on 2021-12-10 18:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(default='N/A', max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_entry', models.DateTimeField(default=datetime.datetime(2021, 12, 10, 18, 8, 29, 329825, tzinfo=utc))),
            ],
        ),
    ]
