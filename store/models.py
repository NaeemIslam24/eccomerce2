from django.db import models
from django.contrib.auth.models import User
import random
# Create your models here.


class Customer(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user)

class Product(models.Model):

    productName = models.CharField(max_length=200)
    digital = models.BooleanField()
    price = models.FloatField()
    productImage = models.ImageField()
    productDescription = models.CharField(max_length=400)

    def __str__(self):
        return self.productName



class Order(models.Model):

    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_total_money(self):
        # chid class is inherited here with "self.orderitem_set.all()"
        orderitems = self.orderitem_set.all()
        # sum function can work with tuple and list. Here it is a list
        all = [item.get_total for item in orderitems]

        total = sum(all)
        return total

    @property
    def total_with_tex(self):
        all = self.get_total_money + 2
        return all
    

    #transation id
    @property
    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_items = []
        for i in range(10):
            num = random.choice(number_list)
            code_items.append(num)
        code_string = "".join(str(item) for item in code_items)
        self.transaction_id = code_string
        super().save(*args, **kwargs)


class OrderItem(models.Model):

    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):

        all = self.quantity * self.product.price
     
        return all


