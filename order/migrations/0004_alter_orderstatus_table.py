# Generated by Django 3.2.4 on 2021-06-10 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_orderstatus_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='orderstatus',
            table='order_status',
        ),
    ]