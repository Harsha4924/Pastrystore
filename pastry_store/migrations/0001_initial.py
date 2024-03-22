# Generated by Django 4.2.4 on 2023-09-20 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('category', models.CharField(default='', max_length=20)),
                ('price', models.IntegerField(default=20)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='pastry_store/images')),
                ('cart', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=1)),
            ],
        ),
    ]
