# Generated by Django 5.1 on 2024-08-26 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furApp', '0007_learnmoreclick'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='adoption_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
