# Generated by Django 5.0.7 on 2024-07-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0005_alter_comment_admin_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
