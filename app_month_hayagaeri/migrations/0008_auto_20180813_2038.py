# Generated by Django 2.0.5 on 2018-08-13 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_month_hayagaeri', '0007_hayagaeriplan_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hayagaeriplan',
            name='plan',
            field=models.CharField(blank=True, max_length=50, verbose_name='早帰り予定'),
        ),
    ]
