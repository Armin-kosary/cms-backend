from django.db import models
from User.models import User
from Product.models import Product
import datetime
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True, auto_now_add=True)
    time = models.CharField(max_length=50, null=True, blank=True, editable=False)
    is_verified = models.BooleanField(null=True, default=False)
    content = models.TextField()
    admin_reply = models.TextField(null=True, blank=True)
    comment_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.comment_code)


    def save(self, *args, **kwargs):
        if not self.comment_code:
            last_comment_code = Comment.objects.last()

            if last_comment_code:
                self.comment_code = last_comment_code.comment_code + 1

            elif not last_comment_code:
                self.comment_code = 10000

        if not self.time:
            now = datetime.datetime.now()
            self.time = f"{now.hour}:{now.minute}"
                
        super(Comment, self).save(*args, **kwargs)