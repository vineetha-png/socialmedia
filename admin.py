from django.contrib import admin
from .models import User, Post, Request, Chat, Like, Comment

# Register models in the admin panel
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Request)
admin.site.register(Chat)
admin.site.register(Like)
admin.site.register(Comment)
