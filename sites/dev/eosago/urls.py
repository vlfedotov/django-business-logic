# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import *


urlpatterns = [
    #url('author$', AuthorList.as_view()),
    #url('author/add$', AuthorCreate.as_view()),

    #url('publisher$', PublisherList.as_view()),
    #url('publisher/(?P<pk>\d+)$', PublisherDetail.as_view(), name='publisher-detail'),
    #url('publisher/add$', PublisherCreate.as_view()),

    url('calculations$', CalculationList.as_view()),
    url('calculations/(?P<pk>\d+)$', CalculationDetail.as_view(), name='calculation-detail'),
    url('calculations/add$', CalculationCreate.as_view()),

]
