# Generated by Django 4.0.4 on 2022-06-19 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_purchase_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='room',
            field=models.PositiveSmallIntegerField(verbose_name='номер'),
        ),
    ]
