# Generated by Django 5.0.7 on 2024-07-19 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
