from django.db import models

# Create your models here.

class Discount(models.Model):
    title = models.CharField(max_length=100, null=True)
    percent = models.IntegerField()
    is_active = models.BooleanField()
    discount_code = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        if not self.discount_code:
            last_discount_code = Discount.objects.last()
            if last_discount_code:
                self.discount_code = last_discount_code.discount_code + 1
            elif not last_discount_code:
                self.discount_code = 10000
        super(Discount, self).save(*args, **kwargs)