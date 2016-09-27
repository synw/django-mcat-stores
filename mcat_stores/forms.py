# -*- coding: utf-8 -*-

from django import forms
from mptt.forms import TreeNodeChoiceField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from mcat_stores.models import Store, Area


class StoreForm(forms.ModelForm):
    area = TreeNodeChoiceField(queryset=Area.objects.all())
    
    class Meta:
        model = Store
        exclude = ['created', 'edited']
        widgets = {'description': CKEditorUploadingWidget(config_name='mcat')}