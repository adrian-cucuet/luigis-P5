# Generated by Django 3.2.20 on 2023-07-16 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='country',
            new_name='default_country',
        ),
    ]
