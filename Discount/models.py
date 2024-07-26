from django.db import models
from User.models import User
# Create your models here.

class Discount(models.Model):
    title = models.CharField(max_length=100, null=True)
    percent = models.IntegerField()
    key = models.CharField(max_length=50, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField()
    discount_code = models.IntegerField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.discount_code:
            last_discount_code = Discount.objects.last()
            if last_discount_code:
                self.discount_code = last_discount_code.discount_code + 1
            elif not last_discount_code:
                self.discount_code = 10000
        super(Discount, self).save(*args, **kwargs)