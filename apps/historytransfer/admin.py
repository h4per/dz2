from django.contrib import admin
from apps.historytransfer.models import HistoryTransfer

# Register your models here.

@admin.register(HistoryTransfer)
class HistoryTransferAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'is_completed', 'amount')