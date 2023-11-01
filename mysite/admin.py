from django.contrib import admin
from mysite.models import Post
from mysite.models import Product
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','pub_date')

admin.site.register(Post,PostAdmin)

admin.site.register(Product)
