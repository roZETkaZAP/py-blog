from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from blog.models import Post, User, Commentary
from django.contrib.auth.models import Group


admin.site.register(User)
admin.site.register(Post)
admin.site.register(Commentary)
admin.site.unregister(Group)