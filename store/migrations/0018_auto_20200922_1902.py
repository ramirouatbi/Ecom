# Generated by Django 3.1.1 on 2020-09-22 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_shippingaddress_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='password2',
            field=models.CharField(max_length=200, null=True),
        ),
    ]