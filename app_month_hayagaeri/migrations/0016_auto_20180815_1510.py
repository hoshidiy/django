# Generated by Django 2.0.5 on 2018-08-15 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_month_hayagaeri', '0015_auto_20180813_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateField(),
        ),
    ]
