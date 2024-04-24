from django.contrib import admin
from .models import Blog, Comment, Blogger

# Register your models here.

# admin.site.register(Blog)
# admin.site.register(Comment)
admin.site.register(Blogger)


# Sets up Comments as inline editing on Blog in Admin site
class CommentsInLine(admin.TabularInline):
    model = Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author')

    inlines = [CommentsInLine]
