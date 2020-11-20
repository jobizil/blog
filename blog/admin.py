from django.contrib import admin
from .models import Post

admin.site.register(Post)
admin.site.site_title = 'Blog'
admin.site.site_header = 'Admin Area'
admin.site.index_title = "Django Blog - Admin"
