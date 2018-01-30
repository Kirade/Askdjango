from django.contrib import admin
from .models import Post, Comment, Tag


admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
