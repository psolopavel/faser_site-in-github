# Generated by Django 4.0.4 on 2022-06-20 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_purchase_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='data',
            field=models.DateField(default=datetime.date(2022, 6, 20), verbose_name='день випуска'),
        ),
    ]