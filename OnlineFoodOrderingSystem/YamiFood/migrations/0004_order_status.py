# Generated by Django 3.2.6 on 2021-09-29 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YamiFood', '0003_product_product_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default='0'),
        ),
    ]