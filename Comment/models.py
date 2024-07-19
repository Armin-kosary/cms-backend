from django.db import models
from User.models import User
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    comment_code = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.comment_code:
            last_comment_code = Comment.objects.last().comment_code

            if last_comment_code:
                self.comment_code = last_comment_code + 1

            elif not last_comment_code:
                self.comment_code = 10000
                
        super(Comment, self).save(*args, **kwargs)