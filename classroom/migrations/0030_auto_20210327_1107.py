# Generated by Django 3.1.5 on 2021-03-27 11:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0029_auto_20210327_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date_of_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 27, 11, 7, 1, 44862, tzinfo=utc), null=True),
        ),
    ]