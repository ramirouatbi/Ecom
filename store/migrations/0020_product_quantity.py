# Generated by Django 3.1.1 on 2020-09-22 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_remove_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
