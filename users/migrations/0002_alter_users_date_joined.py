# Generated by Django 4.2.5 on 2024-06-04 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_joined',
            field=models.DateTimeField(default='2024-06-04T12:22:34.619647+07:00', verbose_name='date joined'),
        ),
    ]
