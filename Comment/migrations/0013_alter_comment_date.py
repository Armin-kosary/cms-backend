# Generated by Django 5.0.7 on 2024-07-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0012_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
