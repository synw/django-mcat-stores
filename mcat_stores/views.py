# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.views.generic import ListView
from mcat_stores.models import City, Area, Store
from django.shortcuts import get_object_or_404
from mcat.conf import PAGINATE_BY


class CityView(TemplateView):
    template_name = "mcat_stores/city.html"
    
    def get_context_data(self, **kwargs):
        context = super(CityView, self).get_context_data(**kwargs)
        city = get_object_or_404(City.objects.prefetch_related("areas"), slug=kwargs['city'])
        areas = city.areas.all()
        context['areas'] = areas
        context['city'] = city
        return context
    
    
class AreaView(ListView):
    template_name = "mcat_stores/area.html"
    paginate_by = PAGINATE_BY
    context_object_name = 'stores'
    
    def get_queryset(self, **kwargs):
        self.area = get_object_or_404(Area.objects.select_related("city"), status=0, slug=self.kwargs['area'])
        q = Store.objects.filter(area=self.area, status=0)
        self.city = self.area.city
        return q
        
    def get_context_data(self, **kwargs):
        context = super(AreaView, self).get_context_data(**kwargs) 
        context['area'] = self.area
        context['city'] = self.city
        return context


class StoreView(TemplateView):
    template_name = "mcat_stores/store.html"
    
    def get_context_data(self, **kwargs):
        context = super(StoreView, self).get_context_data(**kwargs)
        store = get_object_or_404(Store.objects.prefetch_related("products__category"), slug=kwargs['store']) 
        context['store'] = store
        context['products'] = store.products.all()
        return context
    

  
