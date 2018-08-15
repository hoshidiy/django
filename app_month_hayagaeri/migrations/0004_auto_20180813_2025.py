# Generated by Django 2.0.5 on 2018-08-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_month_hayagaeri', '0003_auto_20180813_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hayagaeri',
            name='plan',
            field=models.CharField(choices=[('', 'NoPlanDay'), ('○', 'PlanDay'), ('早週', 'HayagaeriWeek')], max_length=50, verbose_name='予定'),
        ),
        migrations.AlterField(
            model_name='hayagaeri',
            name='result',
            field=models.CharField(choices=[('◎', 'HayagaeriSuccess'), ('×', 'HayagaeriFailed')], max_length=50, verbose_name='結果'),
        ),
    ]
