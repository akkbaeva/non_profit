from django.contrib import admin

# Register your models here.
from npo_consultation.models import Question, Answer

admin.site.register(Question)
admin.site.register(Answer)
