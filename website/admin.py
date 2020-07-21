from django.contrib import admin
from .models import *
from django.contrib.auth.models import User


# Register your models here.
class ProfileAdmin(admin.TabularInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileAdmin, ]


admin.site.register(Profile)
admin.site.register(CarImages)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Maker)
admin.site.register(Model)
admin.site.register(Car)
admin.site.register(Transmission)
admin.site.register(Color)
admin.site.register(Cylinder)
admin.site.register(Fuel)
admin.site.register(Drivetrain)
admin.site.register(SellerType)
admin.site.register(Body)
admin.site.register(AdViews)
