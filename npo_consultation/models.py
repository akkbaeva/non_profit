from django.db import models

# Create your models here.
from npo_user.models import NPOUser


class Question(models.Model):
    user = models.ForeignKey(NPOUser, on_delete=models.CASCADE, null=True)
    text = models.TextField()

    def __str__(self):
        return self.text

    def filter(self):
        return Answer.objects.filter(text=id)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    text = models.TextField()

    def __str__(self):
        return self.text
