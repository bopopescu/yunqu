# uncompyle6 version 3.2.3
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.5 (default, Jul 13 2018, 13:06:57) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)]
# Embedded file name: ./sqlaudit/migrations/0009_auto_20171213_0950.py
# Compiled at: 2018-08-23 19:33:14
# Size of source mod 2**32: 971 bytes
from __future__ import unicode_literals
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
     ('sqlaudit', '0008_auto_20171212_1224')]
    operations = [
     migrations.AddField(model_name='audit_rule',
       name='name',
       field=models.CharField(max_length=100, null=True)),
     migrations.AddField(model_name='audit_rule',
       name='sql_template',
       field=models.CharField(max_length=1000, null=True)),
     migrations.AddField(model_name='audit_strategy',
       name='target',
       field=models.CharField(max_length=100, null=True)),
     migrations.AlterField(model_name='optimization_job',
       name='status',
       field=models.IntegerField(null=True))]
# okay decompiling ./restful/hawkeye/sqlaudit/migrations/0009_auto_20171213_0950.pyc
