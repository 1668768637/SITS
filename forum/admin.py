from django.contrib import admin
from .models import Post,PostImage,userCollection,Message,Commit

# Register your models here.
class PostImgInline(admin.StackedInline):
    model = PostImage


class PostAdmin(admin.ModelAdmin):
    #inlines = [PostImgInline,CommitInline]
    inlines = [PostImgInline]

class CommitAdmin(admin.ModelAdmin):
    list_display = ('context','isChecked')
    ordering = ('isChecked',)

    
admin.site.register(Commit,CommitAdmin)

admin.site.register(Post, PostAdmin)

admin.site.register(userCollection)

admin.site.register(Message)