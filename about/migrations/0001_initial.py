# Generated by Django 3.2.20 on 2023-07-21 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_number', models.CharField(editable=False, max_length=6, null=True, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('no_of_guests', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('12.00 - 13.00', '12.00 - 13.00'), ('13.00 - 14.00', '13.00 - 14.00'), ('14.00 - 15.00', '14.00 - 15.00'), ('15.00 - 16.00', '15.00 - 16.00'), ('16.00 - 17.00', '16.00 - 17.00'), ('17.00 - 18.00', '17.00 - 18.00'), ('18.00 - 19.00', '18.00 - 19.00'), ('19.00 - 20.00', '19.00 - 20.00'), ('20.00 - 21.00', '20.00 - 21.00')], default=('12.00 - 13.00', '12.00 - 13.00'), max_length=15)),
            ],
        ),
    ]