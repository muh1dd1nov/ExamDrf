from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import Post, Image , Comment, SavedPost, User

admin.site.register(Post)   
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(SavedPost)  
