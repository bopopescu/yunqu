# uncompyle6 version 3.2.3
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.5 (default, Jul 13 2018, 13:06:57) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)]
# Embedded file name: ./monitor/migrations/0021_auto_20180119_1439.py
# Compiled at: 2018-08-23 19:33:14
# Size of source mod 2**32: 415 bytes
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
     ('monitor', '0020_database_is_switch_off')]
    operations = [
     migrations.AlterField(model_name='database',
       name='alias',
       field=models.CharField(default='', max_length=100, null=True))]
# okay decompiling ./restful/hawkeye/monitor/migrations/0021_auto_20180119_1439.pyc
