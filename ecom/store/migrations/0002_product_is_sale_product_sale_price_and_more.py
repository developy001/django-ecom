# Generated by Django 5.0.6 on 2024-09-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_sale",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="product",
            name="sale_price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name="customer",
            name="email",
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name="customer",
            name="password",
            field=models.CharField(max_length=50),
        ),
    ]
