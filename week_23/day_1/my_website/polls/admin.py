from django.contrib import admin
from polls.models import Post, Email, Address


# Register your models here.
admin.site.register(Post)
admin.site.register(Email)
admin.site.register(Address)
