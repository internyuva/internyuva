# Generated by Django 3.1.5 on 2021-03-27 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_account_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewslettersSubscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
            ],
        ),
    ]
