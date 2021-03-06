# uncompyle6 version 3.2.3
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.5 (default, Jul 13 2018, 13:06:57) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)]
# Embedded file name: ./delete_history_tasks.py
# Compiled at: 2018-08-23 19:33:14
# Size of source mod 2**32: 580 bytes
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hawkeye.settings.prod')
import django
django.setup()
from django_celery_beat.models import PeriodicTask
count = (PeriodicTask.objects.filter(name__in=['', ''])).count()
print('Number of invalid tasks to be removed:' + str(count))
try:
    (PeriodicTask.objects.filter(name__in=['', ''])).delete()
except:
    print('Tasks deletion failed')

print('Tasks deletion success')
# okay decompiling ./restful/hawkeye/delete_history_tasks.pyc
