# Generated by Django 5.0.7 on 2024-07-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
