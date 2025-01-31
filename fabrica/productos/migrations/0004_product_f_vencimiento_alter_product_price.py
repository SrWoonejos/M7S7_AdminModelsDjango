# Generated by Django 5.1.5 on 2025-01-31 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='f_vencimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
