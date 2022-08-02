# Generated by Django 4.0.6 on 2022-07-31 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price_compare_app', '0002_remove_phone_price_komga_phone_price_konga_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='phone',
        ),
        migrations.CreateModel(
            name='wishitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='price_compare_app.phone')),
                ('wish', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='price_compare_app.wishlist')),
            ],
        ),
    ]
