# Generated by Django 4.2.5 on 2024-06-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_users_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_joined',
            field=models.DateTimeField(default='2024-06-06T18:40:01.786423+07:00', verbose_name='date joined'),
        ),
        migrations.DeleteModel(
            name='Token',
        ),
    ]