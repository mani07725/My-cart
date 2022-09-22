# to start the shell run python manage.py shell 
# then import the models file as from shop.models import Product
# then for creating a new product or new object we use then command
# myprod= Product(product_name="mouse", category="computer",subcategory="devices", price=12, desc="ya aik chouha ha", pub_date=timezone.now()) 
# for saving this object to the databasewe use myprod.save()
# for retrieving a specific information in the databasewe we use the get function as follow
# Product.objects.get(product_name="mouse")
# inside the brackets we define a filter for which object we want to retrive information in this way we can query into the database and alter anything
# for loops we use{%for i in range%} and for variables we use {{variables}} in django we use this in html files