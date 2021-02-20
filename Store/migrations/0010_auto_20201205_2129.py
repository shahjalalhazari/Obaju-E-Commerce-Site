# Generated by Django 3.0 on 2020-12-06 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Store', '0009_auto_20201205_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='review_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
