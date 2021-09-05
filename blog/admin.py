from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Category)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('headline','slug','author','active','published')
    prepopulated_fields = {'slug':('headline',)}