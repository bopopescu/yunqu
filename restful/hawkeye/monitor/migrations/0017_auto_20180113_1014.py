# uncompyle6 version 3.2.3
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.5 (default, Jul 13 2018, 13:06:57) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)]
# Embedded file name: ./monitor/migrations/0017_auto_20180113_1014.py
# Compiled at: 2018-08-23 19:33:14
# Size of source mod 2**32: 911 bytes
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
     ('monitor', '0016_auto_20180112_2045')]
    operations = [
     migrations.AddField(model_name='oracle_ash',
       name='blocking_session',
       field=models.IntegerField(null=True)),
     migrations.AddField(model_name='oracle_ash',
       name='blocking_session_serial',
       field=models.IntegerField(null=True)),
     migrations.AddField(model_name='oracle_ash',
       name='sql_plan_line_id',
       field=models.IntegerField(null=True)),
     migrations.AddField(model_name='oracle_ash',
       name='sql_plan_operation',
       field=models.CharField(max_length=200, null=True))]
# okay decompiling ./restful/hawkeye/monitor/migrations/0017_auto_20180113_1014.pyc
