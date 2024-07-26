from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title

class User(AbstractUser):
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    score = models.CharField(max_length=50)
    buy = models.CharField(max_length=50)
    user_code = models.IntegerField(null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.user_code:
            last_user_code = User.objects.last()
            if last_user_code:
                self.user_code = last_user_code.user_code + 1
            elif not last_user_code:
                self.user_code = 10000
        super(User, self).save(*args, **kwargs)