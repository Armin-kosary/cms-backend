# Generated by Django 5.0.7 on 2024-07-23 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0017_alter_comment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True),
        ),
    ]