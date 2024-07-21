from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    score = models.CharField(max_length=50)
    buy = models.CharField(max_length=50)
    user_code = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.user_code:
            last_user_code = User.objects.last()
            if last_user_code:
                self.user_code = last_user_code.user_code + 1
            elif not last_user_code:
                self.user_code = 10000
        super(User, self).save(*args, **kwargs)

    USERNAME_FIELD = "username"