# Generated by Django 5.0.7 on 2024-07-23 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0014_alter_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]