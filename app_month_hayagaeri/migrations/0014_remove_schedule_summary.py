# Generated by Django 2.0.5 on 2018-08-13 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_month_hayagaeri', '0013_auto_20180813_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='summary',
        ),
    ]
