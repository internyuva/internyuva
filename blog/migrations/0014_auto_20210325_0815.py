# Generated by Django 3.1.5 on 2021-03-25 08:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210325_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 8, 15, 21, 287901, tzinfo=utc)),
        ),
    ]
