# Generated by Django 3.0 on 2021-02-15 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0005_auto_20210214_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='name',
            field=models.CharField(choices=[('PAYPAL', 'PayPal'), ('CARD', 'Card'), ('COD', 'Cash On Delivary')], max_length=10),
        ),
    ]
