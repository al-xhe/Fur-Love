# Generated by Django 5.1 on 2024-08-23 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furApp', '0003_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
