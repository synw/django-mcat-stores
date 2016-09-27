# -*- coding: utf-8 -*-

from django.conf.urls import url
from mcat_stores.views import CityView, AreaView, StoreView

urlpatterns = [
    url(r'^city/(?P<city>[-_\w]+)/$', CityView.as_view(), name="stores-city"),
    url(r'^area/(?P<area>[-_\w]+)/$', AreaView.as_view(), name="stores-area"),
    url(r'^store/(?P<store>[-_\w]+)/$', StoreView.as_view(), name="stores-store"),
    ]


