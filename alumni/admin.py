from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.db.models import Sum
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
	list_display = ('firstName', 'lastName', 'graduationYear',
					'otherDegrees', 'profession', 'board',
					'positionHeld', 'full_address', 'city',
					'state', 'zipCode', 'email1', 'dateAdded')
	list_filter = ['state', 'graduationYear', 'board', 'positionHeld', 'article', 'followed', 'formCategory']
	search_fields = ['firstName', 'middleName', 'lastName', 'nickName']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date','published_by']
    def published_by(self, obj):
        return obj.user
    published_by.short_description = 'Published By'
    published_by.admin_order_field = 'user'
    search_fields = ['title']
    list_filter = ['pub_date']

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
