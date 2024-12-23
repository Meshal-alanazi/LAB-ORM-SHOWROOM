# Generated by Django 5.1.1 on 2024-11-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('brand', models.CharField(max_length=300)),
                ('color', models.CharField(max_length=200)),
                ('photo', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('space', models.TextField()),
                ('model_year', models.PositiveIntegerField()),
                ('fuel_type', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')], default='Petrol', max_length=50)),
            ],
        ),
    ]
