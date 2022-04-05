from django.contrib import admin
from post.models import Post,Follow,Stream
# Register your models here.


admin.site.register(Post)

admin.site.register(Follow)
admin.site.register(Stream)