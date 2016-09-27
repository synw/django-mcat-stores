# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from jsonfield import JSONField
from mptt.models import TreeForeignKey, MPTTModel
from mbase.models import MetaBaseModel, MetaBaseUniqueSlugModel, MetaBaseNameModel, MetaBaseStatusModel
from mcat.models import Product


class City(MetaBaseModel, MetaBaseUniqueSlugModel, MetaBaseNameModel, MetaBaseStatusModel):
    country = models.CharField(max_length=120, null=True, blank=True, verbose_name=_(u'Country'))
    
    class Meta:
        verbose_name=_(u"City")
        verbose_name_plural = _(u"Cities")

    def __unicode__(self):
        return unicode(self.name)
    

class Area(MPTTModel, MetaBaseModel, MetaBaseUniqueSlugModel, MetaBaseNameModel, MetaBaseStatusModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name=u'children', verbose_name=_(u'Parent area'))
    city = models.ForeignKey(City, blank=False, related_name='areas', null=True, verbose_name=_(u"City")) 
    
    class Meta:
        verbose_name= _(u"Area")
        verbose_name_plural = _(u"Areas")
        ordering = ('city',)

    def __unicode__(self):
        return unicode(self.name)
    

class Store(MetaBaseModel, MetaBaseUniqueSlugModel, MetaBaseNameModel, MetaBaseStatusModel):
    city = models.ForeignKey(City, blank=False, null=True, verbose_name=_(u"City"))   
    area = models.ForeignKey(Area, null=True, blank=True, verbose_name=_(u"Area"))   
    products = models.ManyToManyField(Product, blank=True, verbose_name=_(u'Products'))
    description = models.TextField(null=True, blank=True, verbose_name=_(u'Description'))
    # location
    longitude = models.FloatField(null=True, blank=True, verbose_name=_(u"Longitude"))
    latitude = models.FloatField(null=True, blank=True, verbose_name=_(u"Latitude"))
    directions = models.TextField(null=True, blank=True, verbose_name=_(u'Directions'))
    # extra data
    data = JSONField(blank=True, verbose_name=_(u'Extra data (json format)'))
    
    class Meta:
        verbose_name=_(u"Store")
        verbose_name_plural = _(u"Stores")
        ordering = ('city', 'area')

    def __unicode__(self):
        return unicode(self.name)