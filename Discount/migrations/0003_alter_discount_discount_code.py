# Generated by Django 5.0.7 on 2024-07-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discount', '0002_discount_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='discount_code',
            field=models.IntegerField(blank=True),
        ),
    ]
