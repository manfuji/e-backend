from django.contrib import admin

from Allmodels.models import Comment, PostModel

# Register your models here.
@admin.register(PostModel)
class ModelAdmin(admin.ModelAdmin):
    link_display_link = ("id","Title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    link_display_link = ("id","Commented_By")

    