from django.contrib import admin
from .models import *

class UserRatingInline(admin.TabularInline):
    model = UserRating

class HobbiesInline(admin.StackedInline):
    model = Hobbies.user.through
# @admin.display(description="ФИО")
# def upper_case_name(obj):
#     return f"{obj.name} {obj.surname}".upper()

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    fields = [('name','surname'),'age','email','sex','city']
    list_display = ['name','surname','age','sex','city']
    list_display_links = ['name','surname']
    list_editable = ["age","city"]
    ordering = ['name']
    list_per_page = 10
    list_filter = ['age','city']
    inlines = [
        UserRatingInline,
        HobbiesInline,
    ]
# admin.site.register (Users,UsersAdmin)
admin.site.register (UserRating)
admin.site.register (Hobbies)
admin.site.register (Establishments)
admin.site.register (EstablishmentsRating)
admin.site.register (Passport)
admin.site.register (Arrangements)
admin.site.register(Host)
admin.site.register (Guest)
# Register your models here.
