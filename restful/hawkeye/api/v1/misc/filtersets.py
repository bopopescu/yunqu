# uncompyle6 version 3.2.3
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.5 (default, Jul 13 2018, 13:06:57) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)]
# Embedded file name: ./api/v1/misc/filtersets.py
# Compiled at: 2018-08-23 19:33:14
# Size of source mod 2**32: 305 bytes
from django.contrib.contenttypes.models import ContentType
import rest_framework_filters as filters

class ContentTypeFilterSet(filters.FilterSet):

    class Meta:
        model = ContentType
        fields = {'app_label':('exact', 'in'), 
         'model':('exact', 'in')}
# okay decompiling ./restful/hawkeye/api/v1/misc/filtersets.pyc
