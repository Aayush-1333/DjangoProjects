from django.db import models


# Create your models here.
class UserAccount(models.Model):
    """User accounts"""
    accountID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, default='user')
    email = models.CharField(max_length=90, default='')
    phone = models.IntegerField(default=0)
    password = models.CharField(max_length=10, default='12345678')
    account_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Details of the product"""
    id = models.IntegerField(primary_key=True, default=0)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=800)
    published_date = models.DateField()
    image = models.ImageField(upload_to="ShadzStore/images", default="")

    def __str__(self):
        return self.product_name


class Complaint(models.Model):
    """Complaints of the customers"""
    complaint_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default='')
    email = models.CharField(max_length=30, default='')
    phone = models.IntegerField(default=0)
    desc = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name


class OrderUpdate(models.Model):
    """Updates after placing order - status of shipments"""
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=0)
    update_desc = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_id}: {self.update_desc[:9]}" + "..."


class OrderDetail(models.Model):
    """Details of the placed orders"""
    order_id = models.AutoField(primary_key=True)
    amount = models.IntegerField(default=0)
    full_name = models.CharField(max_length=90, default="NA")
    address1 = models.CharField(max_length=80, default="")
    address2 = models.CharField(max_length=80, default="")
    address3 = models.CharField(max_length=80, default="")
    state = models.CharField(max_length=40, default="")
    city = models.CharField(max_length=20, default="")
    zipcode = models.CharField(max_length=7, default="")
    contact_number = models.CharField(max_length=13, default="")
    email_address = models.CharField(max_length=90, default="")

    def __str__(self):
        return f"{self.full_name}: {self.order_id}"
