# uncompyle6 version 3.2.3
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.5 (default, Jul 13 2018, 13:06:57) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)]
# Embedded file name: ./sqlaudit/migrations/0022_auto_20171218_1757.py
# Compiled at: 2018-08-23 19:33:14
# Size of source mod 2**32: 478 bytes
from __future__ import unicode_literals
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
     ('sqlaudit', '0021_auto_20171218_1303')]
    operations = [
     migrations.AlterField(model_name='audit_sql_text',
       name='sql_text',
       field=models.TextField(max_length=3000000, null=True))]
# okay decompiling ./restful/hawkeye/sqlaudit/migrations/0022_auto_20171218_1757.pyc
