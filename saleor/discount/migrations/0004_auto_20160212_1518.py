# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0003_auto_20160207_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='type',
            field=models.CharField(choices=[('fixed', 'INR'), ('percentage', '%')], default='fixed', max_length=10),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='discount_value_type',
            field=models.CharField(choices=[('fixed', 'INR'), ('percentage', '%')], default='fixed', max_length=10, verbose_name='discount type'),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='limit',
            field=django_prices.models.PriceField(blank=True, currency='INR', decimal_places=2, max_digits=12, null=True),
        ),
    ]
