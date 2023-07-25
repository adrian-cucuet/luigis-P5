# Generated by Django 3.2.20 on 2023-07-24 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name_plural': 'Variants',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='topping',
        ),
        migrations.AddField(
            model_name='product',
            name='variant',
            field=models.CharField(choices=[('None', 'None'), ('Size', 'Size')], default='None', max_length=10),
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
        migrations.AddField(
            model_name='variants',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
        migrations.AddField(
            model_name='variants',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.size'),
        ),
    ]
