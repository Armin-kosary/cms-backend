from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=500)
    price = models.IntegerField()
    count = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Product-Images/')
    popularity = models.CharField(max_length=50)
    sale_amount = models.CharField(max_length=50)
    colors = models.CharField(max_length=100, null=True)
    product_code = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.product_code:
            last_product_code = Product.objects.last()

            if last_product_code:
                self.product_code = last_product_code.product_code + 1

            elif not last_product_code:
                self.product_code = 10000

        super(Product, self).save(*args, **kwargs)