# Generated by Django 4.2 on 2023-04-27 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrangement', '0004_alter_establishments_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishments',
            name='address',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='establishments',
            name='phone',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='passport',
            name='date_create',
            field=models.DateTimeField(auto_created=datetime.datetime(2023, 4, 27, 12, 59, 47, 748902)),
        ),
        migrations.AddIndex(
            model_name='establishments',
            index=models.Index(fields=['name', 'category'], name='arrangement_name_7ed026_idx'),
        ),
        migrations.AddIndex(
            model_name='guest',
            index=models.Index(fields=['min_bill_value'], name='arrangement_min_bil_fc65a0_idx'),
        ),
        migrations.AddIndex(
            model_name='host',
            index=models.Index(fields=['max_spent_value'], name='arrangement_max_spe_30f636_idx'),
        ),
    ]
