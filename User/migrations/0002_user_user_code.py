# Generated by Django 5.0.7 on 2024-07-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_code',
            field=models.IntegerField(null=True),
        ),
    ]