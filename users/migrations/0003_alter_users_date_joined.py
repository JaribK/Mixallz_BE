# Generated by Django 4.2.5 on 2024-06-04 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_joined',
            field=models.DateTimeField(default='2024-06-04T13:33:22.313655+07:00', verbose_name='date joined'),
        ),
    ]