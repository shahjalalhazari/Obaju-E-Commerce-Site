# Generated by Django 3.0 on 2020-11-27 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_auto_20201126_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extraimgs',
            options={'verbose_name_plural': 'Extra Images'},
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]