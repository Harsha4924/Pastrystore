from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20, default="")
    price = models.IntegerField(default=20)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pastry_store/images')
    cart = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=1)

    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name_plural = "Products"

class ItemsDelivery(models.Model):
    order_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=23)
    contact_number = models.CharField(max_length=10, validators=[
        MaxLengthValidator(limit_value=10, message='Contact number should not be greater than 10 digits.'),
        MinLengthValidator(limit_value=10, message='Contact number should not be less than 10 digits.')
    ])
    address = models.TextField()  # Use TextField for address
    zip_code = models.CharField(max_length=6, validators=[
        MaxLengthValidator(limit_value=6, message='Zip code should not be greater than 6 digits.'),
        MinLengthValidator(limit_value=6, message='Zip code should not be less than 6 digits.')
    ])
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)