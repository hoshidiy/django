# Generated by Django 2.0.5 on 2018-08-13 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_month_hayagaeri', '0005_auto_20180813_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='hayagaeri',
            new_name='hayagaeri_plan',
        ),
        migrations.AlterField(
            model_name='hayagaeriplan',
            name='plan',
            field=models.CharField(max_length=50, verbose_name='早帰り予定'),
        ),
    ]
