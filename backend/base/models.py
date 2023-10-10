from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    # Foreign Keys
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    #Char Fields
    name = models.CharField(max_length=200, null=True, blank=True)
    brand =  models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # Text Fields
    description = models.TextField(null=True, blank=True)

    # Decimal Fields
    rating = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    # Integer Fields
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    countInStock = models.IntegerField(null=True, blank=True, default=0)

    # Date Time Fields
    createdAt = models.DateTimeField(auto_now_add=True)

    # Primary Key
    _id = models.AutoField(primary_key=True, editable=False)

    # Methods
    def __str__(self):
        return self.name

class Review(models.Model):
    # Foreign Keys
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    # Integer Fields
    rating = models.IntegerField(null=True, blank=True, default=0)

    # Character Firelds
    name = models.CharField(max_length=200, null=True, blank=True)

    # Text Fields
    comment = models.TextField(null=True, blank=True)

    # Date Time Fields
    createdAt = models.DateTimeField(auto_now_add=True)

    # Primary Key
    _id = models.AutoField(primary_key=True, editable=False)

    # Methods
    def __str__(self):
        return str(self.rating)

class Order(models.Model):
    # Foreign Keys
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    # Char Fields
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)

    # Decimal Fields
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

    # Boolean Fields
    isPaid = models.BooleanField(default=False)
    isDelivered = models.BooleanField(default=False)

    # Date Time Fields
    paidAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    deliveredAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    # Primary Key
    _id = models.AutoField(primary_key=True, editable=False)

    # Methods
    def __str__(self):
        return str(self._id)

class OrderItem(models.Model):
    # Foreign Keys
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    # Integer Fields
    qty = models.IntegerField(null=True, blank=True, default=0)

    # Character Fields
    image = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)

    # Decimal Fields
    price = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

    # Primary Key
    _id = models.AutoField(primary_key=True, editable=False)

    # Methods
    def __str__(self):
        return str(self.name)

class ShippingAddress(models.Model):
    # Foreign Keys
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)

    # Character Fields
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    # Decimal Fields
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

    # Primary Key
    _id = models.AutoField(primary_key=True, editable=False)

    # Methods
    def __str__(self):
        return self.address
