# Generated by Django 2.0.5 on 2018-08-13 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_month_hayagaeri', '0008_auto_20180813_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='hayagaeri_plan',
        ),
        migrations.DeleteModel(
            name='HayagaeriPlan',
        ),
    ]