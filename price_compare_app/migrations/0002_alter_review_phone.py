# Generated by Django 4.0.6 on 2022-08-06 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price_compare_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='price_compare_app.phone'),
        ),
    ]
