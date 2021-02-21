# Generated by Django 3.0 on 2021-02-20 11:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_auto_20210220_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderId',
            field=models.UUIDField(default=uuid.uuid1, editable=False),
        ),
    ]