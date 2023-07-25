from django.contrib import admin
from .models import Phone

# Register your models here.

class PhoneAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "image","release_date","lte_exists")
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Phone, PhoneAdmin)