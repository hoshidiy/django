# Generated by Django 2.0.5 on 2018-08-15 06:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_month_hayagaeri', '0016_auto_20180815_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
