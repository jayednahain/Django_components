from django.contrib import admin

# Register your models here.
from .models import LOG_OUT_SIGNALS,LOG_IN_SIGNALS,LOGIN_FAILED

# admin.site.register(LOG_OUT_SIGNALS)
# admin.site.register(LOG_IN_SIGNALS)


@admin.register(LOG_IN_SIGNALS)
class PurchaseAdmin(admin.ModelAdmin):
   list_display = ['id','sender','request_path','username','created_time']

@admin.register(LOG_OUT_SIGNALS)
class PurchaseAdmin(admin.ModelAdmin):
   list_display = ['id','sender','request_path','username','created_time']


@admin.register(LOGIN_FAILED)
class PurchaseAdmin(admin.ModelAdmin):
   list_display = ['id','sender','request_path','username','created_time']
