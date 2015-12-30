# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter(trailing_slash=False)
#router.register(r'users', UserViewSet)
#router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls
urlpatterns = [
    url('^$', api_root, name='root'),
    url('^program-type$', ProgramTypeList.as_view(), name='program-type-list'),
    url('^program-type/(?P<pk>\d+)$', ProgramTypeView.as_view(), name='program-type'),
    url('^reference/descriptor$', ReferenceDescriptorList.as_view(), name='reference-descriptor-list'),
    url('^reference/list/(?P<model>[\w.]+)$', ReferenceList.as_view(), name='reference-list'),
    url('^program-version/(?P<pk>\d+)$', program_version_view, name='program-version'),
]

