# Generated by Django 5.1.1 on 2024-11-21 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Model',
            new_name='Car',
        ),
    ]
