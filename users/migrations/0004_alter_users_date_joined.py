# Generated by Django 4.2.5 on 2024-06-05 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_users_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_joined',
            field=models.DateTimeField(default='2024-06-05T17:52:26.860447+07:00', verbose_name='date joined'),
        ),
    ]
