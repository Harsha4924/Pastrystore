# Generated by Django 4.2.4 on 2023-09-25 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastry_store', '0002_items_delivery_alter_products_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items_delivery',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='items_delivery',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]
