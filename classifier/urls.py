# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 16:36:10 2014

@author: davidp
"""

from django.conf.urls import patterns, url
from classifier import views

urlpatterns = patterns('',
    url(r'^api/synonyms$', views.get_synonyms, name='synonyms'),
    url(r'^api/hyponyms$', views.get_hyponyms, name='hyponyms'),
    url(r'^api/hypernyms$', views.get_hypernyms, name='hypernyms')
)