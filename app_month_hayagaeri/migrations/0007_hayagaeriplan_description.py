# Generated by Django 2.0.5 on 2018-08-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_month_hayagaeri', '0006_auto_20180813_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='hayagaeriplan',
            name='description',
            field=models.TextField(blank=True, verbose_name='詳細な説明'),
        ),
    ]