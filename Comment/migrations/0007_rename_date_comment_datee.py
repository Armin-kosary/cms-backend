# Generated by Django 5.0.7 on 2024-07-23 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0006_alter_comment_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='date',
            new_name='datee',
        ),
    ]
