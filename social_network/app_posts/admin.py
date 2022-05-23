from django.contrib import admin
from .models import PostClass


# Register your models here.

class PostClassAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'Title_post', 'time_create', 'user_id')
    list_display_links = ('post_id', 'Title_post')
    search_fields = ('Title_post', 'Full_content')
    list_editable = ('user_id',)
    list_filter = ('user_id', 'time_create')


admin.site.register(PostClass, PostClassAdmin)
