# Generated by Django 3.2.7 on 2021-10-05 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.AutoField(primary_key=True, serialize=False)),
                ('delivery_carrier', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_ordered', models.DateField(auto_now_add=True)),
                ('total_price', models.FloatField()),
                ('status', models.BooleanField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_category', models.CharField(max_length=50)),
                ('product_picture', models.CharField(default='', max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=11)),
                ('is_admin', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('receiver_id', models.AutoField(primary_key=True, serialize=False)),
                ('receiver_name', models.CharField(max_length=100)),
                ('receiver_contact', models.CharField(max_length=11)),
                ('receiver_address', models.CharField(max_length=100)),
                ('date_received', models.DateField()),
                ('time_received', models.TimeField()),
                ('delivery_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YamiFood.delivery')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YamiFood.order')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Details',
            fields=[
                ('order_details_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YamiFood.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YamiFood.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YamiFood.user'),
        ),
    ]
