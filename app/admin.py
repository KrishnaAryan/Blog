from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'content', 'author']
    search_fields = ['title', 'content']
    

admin.site.register(BlogPost, BlogPostAdmin)
