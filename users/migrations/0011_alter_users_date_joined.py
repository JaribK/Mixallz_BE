# Generated by Django 4.2.5 on 2024-06-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_users_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_joined',
            field=models.DateTimeField(default='2024-06-12T00:02:38.822752+07:00', verbose_name='date joined'),
        ),
    ]
