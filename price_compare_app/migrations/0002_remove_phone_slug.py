# Generated by Django 4.0.6 on 2022-08-03 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price_compare_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='slug',
        ),
    ]