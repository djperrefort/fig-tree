from django.contrib import admin

from . import models


class TreePermissionInline(admin.TabularInline):
    """Inline admin element for family tree user permissions"""

    model = models.TreePermission
    show_change_link = False
    extra = 0


@admin.register(models.Tree)
class TreeAdmin(admin.ModelAdmin):
    """Admin interface for family tree objects"""

    list_display = ('tree_name',)
    inlines = [TreePermissionInline]
    search_fields = ['tree_name']
    ordering = ['tree_name']
