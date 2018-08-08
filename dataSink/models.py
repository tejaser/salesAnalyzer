from django.db import models
from django.utils import timezone
# Create your models here.
customer_type = (
    ('STOCKIST', 'Stockist'),
    ('WHOLESALER', 'Wholesaler'),
    ('DISTRIBUTOR', 'Distributor'))


customer_status = (
    ('LIVE', 'Live'),
    ('ACTIVE', 'Active'),
    ('OLD', 'Old'),
    ('BLACKLISTED', 'Black_listed'),
    ('OTHER', 'Other'))

product_series = (
    ('RUSTIC', 'Rustic'),
    ('SATIN', 'Satin'),
    ('MATT', 'Matt'),
    ('GLOSSY', 'Glossy'),
    ('WOOD', 'Wood'),
    ('PUNCH', 'Punch'))

product_grade = (
    ('PREMIUM', 'Premium(1st Grade)'),
    ('STANDARD', 'Standard'),
    ('COMMERCE', 'Commerce'),
    ('LASTGRADE', '4th Grade'))

product_category = (
    ('CAT1', 'Category1'),
    ('CAT2', 'Category2'),
    ('CAT3', 'Category3')
     )

class dispatchOrder(models.Model):
    do_id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    do_number = models.BigIntegerField()
    dispatch_date = models.DateTimeField(
        default=timezone.now)
    customer_name = models.CharField(max_length=100)
    group_name = models.CharField(max_length=70, blank=True, null=True)
    ref_name = models.CharField(max_length=70, blank=True, null=True)
    city = models.CharField(default='', max_length=70)
    address = models.TextField(default='')
    product_code = models.TextField()
    product_category = models.TextField()
    product_brand = models.CharField(max_length=70, default='')
    prodcut_series = models.CharField(max_length=70, default='')
    product_class = models.CharField(max_length=70, default='')

    def __str__(self):
        return self.customer_name


class customerRegistration(models.Model):
    cust_id = models.BigAutoField(primary_key=True)
    cust_name = models.CharField(max_length=70)
    person_name = models.CharField(max_length=70)
    cust_address = models.TextField(default='')
    cust_city = models.CharField(default='', max_length=70)
    cust_state = models.CharField(default='',max_length=70)
    cust_pin_code = models.IntegerField(default=0)
    cust_phone_number = models.IntegerField(default=0)
    cust_tin_number = models.CharField(default=0,max_length=70)
    cust_pan_number = models.CharField(default=0,max_length=70)
    cust_email = models.EmailField()
    cust_reference = models.TextField(default='')
    mrp_zone = models.CharField(max_length=70)
    area_cover = models.CharField(max_length=70)
    area_cover_pincode = models.IntegerField(default=0)
    customer_type = models.CharField(choices=customer_type, default='Stockist',max_length=10)
    customer_status = models.CharField(choices=customer_status, default='Active',max_length=10)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(blank=True, null=True, max_length=70)

    def update(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return self.cust_name


class productForm(models.Model):
    prodcut_id = models.BigAutoField(primary_key=True)
    product_series = models.CharField(choices=product_series, default='Rustic', max_length=10)
    product_code = models.CharField(max_length=70, default='')
    product_class = models.CharField(choices=product_grade, default='Standard', max_length=10)
    product_category = models.CharField(choices=product_category, default='CAT1',max_length=10)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=0)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_series + ' ' + str(self.prodcut_id)

