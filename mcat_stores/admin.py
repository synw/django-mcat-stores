# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from mcat_stores.models import City, Area, Store
from mcat_stores.forms import StoreForm


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    date_hierarchy = 'edited'
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name', 'editor__username']
    readonly_fields = ['editor']
    fields = ['name', 'slug', 'country', 'editor', 'status']
    list_display = ['name', 'edited', 'editor', 'status']
    list_select_related = ['editor']
    radio_fields = {"status": admin.HORIZONTAL}
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'editor', None) is None:
            obj.editor = request.user
        obj.save()


@admin.register(Area)
class AreaAdmin(DraggableMPTTAdmin):
    date_hierarchy = 'edited'
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name', 'editor__username', 'city__name', 'parent__name']
    readonly_fields = ['editor']
    fields = ['name', 'slug', 'city', 'parent', 'editor', 'status']
    list_display = ['tree_actions', 'indented_title', 'name', 'city', 'parent', 'edited', 'editor', 'status']
    list_select_related = ['editor', 'city', 'parent']
    list_display_links = ('indented_title',)
    radio_fields = {"status": admin.HORIZONTAL}
    mptt_level_indent = 30

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'editor', None) is None:
            obj.editor = request.user
        obj.save()


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    save_as=True
    save_on_top=True
    form = StoreForm
    date_hierarchy = 'edited'
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name', 'editor__username', 'city__name', 'area__name']
    readonly_fields = ['editor']
    list_display = ['name', 'city', 'area', 'edited', 'editor', 'status']
    list_select_related = ['editor', 'city', 'area']
    filter_horizontal = ('products',)
    radio_fields = {"status": admin.HORIZONTAL}
    fieldsets = (
            (None, {
                'fields': (('name','slug'),)
            }),
            (None, {
                'fields': (('city','area'),)
            }),
            (None, {
                'fields': (('products',),)
            }),
            (_(u"Description"), {
                'classes': ('collapse',),
                'fields': ('description',)
            }),
            (_(u"Location"), {
                'classes': ('collapse',),
                'fields': (('longitude', 'latitude'), ('directions',))
            }),
            (_(u"Extra data"), {
                'classes': ('collapse',),
                'fields': (('data',),)
            }),
            (None, {
                'fields': (('status',), ('editor',),)
            }),
            )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'editor', None) is None:
            obj.editor = request.user
        obj.save()