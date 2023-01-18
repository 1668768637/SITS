from django.contrib import admin
from .models import Post,PostImage

# Register your models here.
class PostImgInline(admin.StackedInline):
    model = PostImage
    extra = 1     # 默认显示条目的数量

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImgInline,]

admin.site.register(Post, PostAdmin)