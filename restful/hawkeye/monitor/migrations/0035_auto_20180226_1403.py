# uncompyle6 version 3.2.3
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.5 (default, Jul 13 2018, 13:06:57) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)]
# Embedded file name: ./monitor/migrations/0035_auto_20180226_1403.py
# Compiled at: 2018-08-23 19:33:14
# Size of source mod 2**32: 5080 bytes
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
     ('monitor', '0034_auto_20180225_2021')]
    operations = [
     migrations.RenameField(model_name='db2_ash',
       old_name='activity_type',
       new_name='command'),
     migrations.RenameField(model_name='db2_ash',
       old_name='appl_id',
       new_name='machine'),
     migrations.RenameField(model_name='db2_ash',
       old_name='appl_name',
       new_name='program'),
     migrations.RenameField(model_name='db2_ash',
       old_name='authid',
       new_name='session_id'),
     migrations.RenameField(model_name='db2_ash',
       old_name='agent_id',
       new_name='sql_elapsed_time'),
     migrations.RenameField(model_name='db2_ash',
       old_name='executable_id',
       new_name='sql_id'),
     migrations.RenameField(model_name='db2_ash',
       old_name='stmt_text',
       new_name='sql_text'),
     migrations.RenameField(model_name='mssql_ash',
       old_name='host_name',
       new_name='machine'),
     migrations.RenameField(model_name='mssql_ash',
       old_name='login_name',
       new_name='program'),
     migrations.RenameField(model_name='mssql_ash',
       old_name='time',
       new_name='sql_elapsed_time'),
     migrations.RenameField(model_name='mssql_ash',
       old_name='sql_handle',
       new_name='sql_id'),
     migrations.RenameField(model_name='mssql_ash',
       old_name='sqltext',
       new_name='sql_text'),
     migrations.RenameField(model_name='mssql_ash',
       old_name='program_name',
       new_name='username'),
     migrations.RenameField(model_name='mysql_ash',
       old_name='db',
       new_name='db_name'),
     migrations.RenameField(model_name='mysql_ash',
       old_name='info',
       new_name='sql_text'),
     migrations.RenameField(model_name='oracle_ash',
       old_name='sqltext',
       new_name='sql_text'),
     migrations.RemoveField(model_name='mysql_ash',
       name='host'),
     migrations.RemoveField(model_name='mysql_ash',
       name='time'),
     migrations.RemoveField(model_name='mysql_ash',
       name='user'),
     migrations.AddField(model_name='db2_ash',
       name='username',
       field=models.CharField(max_length=100, null=True)),
     migrations.AddField(model_name='mysql_ash',
       name='machine',
       field=models.CharField(max_length=100, null=True)),
     migrations.AddField(model_name='mysql_ash',
       name='sql_elapsed_time',
       field=models.IntegerField(null=True)),
     migrations.AddField(model_name='mysql_ash',
       name='username',
       field=models.CharField(max_length=100, null=True)),
     migrations.AddField(model_name='oracle_ash',
       name='session_id',
       field=models.CharField(max_length=100, null=True)),
     migrations.AddField(model_name='oracle_ash',
       name='sql_elapsed_time',
       field=models.BigIntegerField(null=True)),
     migrations.AlterField(model_name='mssql_ash',
       name='session_id',
       field=models.CharField(max_length=100, null=True)),
     migrations.AlterField(model_name='mysql_ash',
       name='command',
       field=models.CharField(max_length=100, null=True)),
     migrations.AlterField(model_name='mysql_ash',
       name='conn_id',
       field=models.IntegerField(null=True)),
     migrations.RemoveField(model_name='db2_ash',
       name='elapsed_time_sec'),
     migrations.AlterIndexTogether(name='db2_ash',
       index_together={
      ('database', 'created_at'), ('machine', 'created_at'), ('sql_id', 'created_at')}),
     migrations.AlterIndexTogether(name='mssql_ash',
       index_together={
      ('database', 'created_at'), ('sql_id', 'created_at'), ('session_id', 'created_at'), ('linked_ip', 'linked_spid')}),
     migrations.AlterIndexTogether(name='oracle_ash',
       index_together={
      ('database', 'created_at'), ('session_id', 'created_at'), ('sql_id', 'created_at')})]
# okay decompiling ./restful/hawkeye/monitor/migrations/0035_auto_20180226_1403.pyc