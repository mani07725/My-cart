import email
from unicodedata import category, name
from django.db import models
# here we have created a schema in the django database this is a  and then merged it in the database  to form a table
# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=3000)
    pub_date = models.DateField()
    # this upload_to means its ganna make a folder in the shop images and save the images that are added to the database in that folder.
    image= models.ImageField(upload_to="shop/images",default="")
# with this line of code the product name is set as it is in the database and object2 and object 2 is not set as product name in the database
    def __str__(self):
        return self.product_name
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70,default=0)
    desc = models.CharField(max_length=3000,default="")
# with this line of code the product name is set as it is in the database and object2 and object 2 is not set as product name in the database
    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=1000)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)

class Order_update(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default='')
    update_description= models.CharField(max_length=5000)
    timestemp=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.update_description[0:7]+ "..."
