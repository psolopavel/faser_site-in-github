# Generated by Django 4.0.4 on 2022-06-23 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_product_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating_star',
            options={'ordering': ['-value'], 'verbose_name': 'звезда рейтинга', 'verbose_name_plural': 'звезди рейтинга'},
        ),
    ]
