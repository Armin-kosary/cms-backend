# Generated by Django 5.0.7 on 2024-07-23 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0008_rename_datee_comment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
    ]
