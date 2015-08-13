# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dailyexpenses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sno', models.IntegerField()),
                ('product', models.CharField(max_length=100)),
                ('purchased_at', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price_id', models.IntegerField()),
                ('product', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('measurement', models.CharField(max_length=20)),
                ('buying_price', models.IntegerField()),
                ('price_per', models.IntegerField()),
                ('local_price', models.IntegerField()),
                ('online_price', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('profit', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sno', models.IntegerField()),
                ('product', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('used_quantity', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vendor_id', models.IntegerField()),
                ('vendor_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('tin', models.CharField(max_length=20)),
                ('account', models.CharField(max_length=20)),
                ('ifsc', models.CharField(max_length=11)),
                ('category', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
