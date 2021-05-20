from django.db import models


# Create your models here.

class Publication(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(blank=True,
                            max_length=200)

    def __str__(self):
        return f'{self.title}'
