# Generated by Django 2.0.8 on 2018-08-18 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_auto_20180818_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='user',
        ),
    ]