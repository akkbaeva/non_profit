from django.contrib import admin

# Register your models here.
from npo_news.models import News


class NewsAdmin(admin.ModelAdmin):
    model = News
    list_filter = 'created_date'.split()
    list_editable = 'title description'.split()
    list_display = 'id title description image link created_date'.split()
    search_fields = 'title description'


admin.site.register(News, NewsAdmin)
