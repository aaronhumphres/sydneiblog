from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin)

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)