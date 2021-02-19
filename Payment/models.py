from django.db import models
from django_countries.fields import CountryField
from django.conf import settings

# SHIPPING ADDRESS MODEL
class ShippingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='billing_address')
    fullname = models.CharField(max_length=300)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    state = models.CharField(max_length=30)
    country = CountryField(max_length=30, blank_label='(select country)')
    phone = models.CharField(max_length=20)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}'s shipping address".format(self.user)
    
    def is_fully_filled(self):
        field_names = [f.name for f in self._meta.get_fields()]
        for field_name in field_names:
            value = getattr(self, field_name)
            if value is None or value =='':
                return False
        return True

    class Meta:
        verbose_name_plural = "Shipping Addresses"


# DELIVERY METHOD MODEL
class DeliveryMethod(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    cost = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


# PAYMENT METHOD MODEL
class PaymentMethod(models.Model):
    NAME_CHOICES = (
        ('PAYPAL', 'PayPal'),
        ('CARD', 'Card'),
        ('COD', 'Cash On Delivary')
    )
    name = models.CharField(choices=NAME_CHOICES, max_length=10)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"