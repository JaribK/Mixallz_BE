# Generated by Django 4.2.5 on 2024-06-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_code_usercoderedemption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='code',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
