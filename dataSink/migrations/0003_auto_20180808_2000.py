# Generated by Django 2.1 on 2018-08-08 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataSink', '0002_auto_20180808_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productform',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
