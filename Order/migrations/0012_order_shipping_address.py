# Generated by Django 3.0 on 2021-02-21 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0007_auto_20210219_1907'),
        ('Order', '0011_auto_20210221_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Payment.ShippingAddress'),
        ),
    ]