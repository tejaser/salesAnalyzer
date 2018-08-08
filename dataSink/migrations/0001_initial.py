# Generated by Django 2.1 on 2018-08-08 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='customerRegistration',
            fields=[
                ('cust_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=70)),
                ('person_name', models.CharField(max_length=70)),
                ('cust_address', models.TextField(default='')),
                ('cust_city', models.CharField(default='', max_length=70)),
                ('cust_state', models.CharField(default='', max_length=70)),
                ('cust_pin_code', models.IntegerField(default=0)),
                ('cust_phone_number', models.IntegerField(default=0)),
                ('cust_tin_number', models.CharField(default=0, max_length=70)),
                ('cust_pan_number', models.CharField(default=0, max_length=70)),
                ('cust_email', models.EmailField(max_length=254)),
                ('cust_reference', models.TextField(default='')),
                ('mrp_zone', models.CharField(max_length=70)),
                ('area_cover', models.CharField(max_length=70)),
                ('area_cover_pincode', models.IntegerField(default=0)),
                ('customer_type', models.CharField(choices=[('STOCKIST', 'Stockist'), ('WHOLESALER', 'Wholesaler'), ('DISTRIBUTOR', 'Distributor')], default='Stockist', max_length=10)),
                ('customer_status', models.CharField(choices=[('LIVE', 'Live'), ('ACTIVE', 'Active'), ('OLD', 'Old'), ('BLACKLISTED', 'Black_listed'), ('OTHER', 'Other')], default='Active', max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=70, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='dispatchOrder',
            fields=[
                ('do_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('do_number', models.BigIntegerField()),
                ('dispatch_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer_name', models.CharField(max_length=100)),
                ('group_name', models.CharField(blank=True, max_length=70, null=True)),
                ('ref_name', models.CharField(blank=True, max_length=70, null=True)),
                ('city', models.CharField(default='', max_length=70)),
                ('address', models.TextField(default='')),
                ('product_code', models.TextField()),
                ('product_category', models.TextField()),
                ('product_brand', models.CharField(default='', max_length=70)),
                ('prodcut_series', models.CharField(default='', max_length=70)),
                ('product_class', models.CharField(default='', max_length=70)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='productForm',
            fields=[
                ('prodcut_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('prodcut_series', models.CharField(choices=[('RUSTIC', 'Rustic'), ('SATIN', 'Satin'), ('MATT', 'Matt'), ('GLOSSY', 'Glossy'), ('WOOD', 'Wood'), ('PUNCH', 'Punch')], default='Rustic', max_length=10)),
                ('product_code', models.CharField(default='', max_length=70)),
                ('product_class', models.CharField(choices=[('PREMIUM', 'Premium(1st Grade)'), ('STANDARD', 'Standard'), ('COMMERCE', 'Commerce'), ('LASTGRADE', '4th Grade')], default='Standard', max_length=10)),
                ('product_category', models.CharField(choices=[('CAT1', 'Category1'), ('CAT2', 'Category2'), ('CAT3', 'Category3')], default='CAT1', max_length=10)),
            ],
        ),
    ]