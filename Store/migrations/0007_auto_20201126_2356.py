# Generated by Django 3.0 on 2020-11-27 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_auto_20201126_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img_1',
            field=models.ImageField(blank=True, null=True, upload_to='ProductImg'),
        ),
        migrations.AddField(
            model_name='product',
            name='img_2',
            field=models.ImageField(blank=True, null=True, upload_to='ProductImg'),
        ),
        migrations.AddField(
            model_name='product',
            name='img_3',
            field=models.ImageField(blank=True, null=True, upload_to='ProductImg'),
        ),
        migrations.AddField(
            model_name='product',
            name='img_4',
            field=models.ImageField(blank=True, null=True, upload_to='ProductImg'),
        ),
        migrations.AddField(
            model_name='product',
            name='img_5',
            field=models.ImageField(blank=True, null=True, upload_to='ProductImg'),
        ),
        migrations.DeleteModel(
            name='ExtraImgs',
        ),
    ]
