# Generated by Django 5.0.7 on 2024-07-21 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
