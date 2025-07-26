# panel/admin/admin.py
from django.contrib import admin
from django.urls import path, include
from django.utils.safestring import mark_safe

def sync_link(obj):
    return mark_safe('<a class="button" href="/admin/sync-db/">🔁 همگام‌سازی دیتابیس</a>')
sync_link.short_description = "ابزار ادمین"

class DummyModel:
    pass

@admin.register(DummyModel)
class DummyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False
    def has_delete_permission(self, request, obj=None): return False

    list_display = [sync_link]
