from django.db import models
from User.models import User
from Product.models import Product
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order_code = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.order_code:
            last_order_code = Order.objects.last()
            if last_order_code:
                self.order_code = last_order_code.order_code + 1
            elif not last_order_code:
                self.order_code = 10000
        super(Order, self).save(*args, **kwargs)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    item_code = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.item_code:
            last_item_code = OrderItem.objects.last()
            if last_item_code:
                self.item_code = last_item_code.item_code + 1
            elif not last_item_code:
                self.item_code = 10000
        super(OrderItem, self).save(*args, **kwargs)