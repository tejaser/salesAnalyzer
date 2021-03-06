# Generated by Django 2.1 on 2018-08-08 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dataSink', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productform',
            old_name='prodcut_series',
            new_name='product_series',
        ),
        migrations.AddField(
            model_name='productform',
            name='created_by',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productform',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
