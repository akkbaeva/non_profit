from django.db import models

# Create your models here.
from npo_user.models import NPOUser


class ICNL(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(max_length=200, blank=True)


class ICNLFavorite(models.Model):
    user = models.ForeignKey(NPOUser, on_delete=models.CASCADE,
                             related_name='saved2', )
    icnl = models.ForeignKey(ICNL, on_delete=models.CASCADE,
                             null=True)
