from django.contrib import admin

from .models import User, Post

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  pass

@admin.register(Post)
class Entry(admin.ModelAdmin):
  pass
