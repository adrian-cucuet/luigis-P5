# Generated by Django 3.2.20 on 2023-07-24 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_remove_orderlineitem_product_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='original_bag',
            new_name='original_cart',
        ),
    ]