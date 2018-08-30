# uncompyle6 version 3.2.3
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.5 (default, Jul 13 2018, 13:06:57) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)]
# Embedded file name: ./sqlaudit/enum/sqlserver_detail_template_enum.py
# Compiled at: 2018-08-23 19:33:14
# Size of source mod 2**32: 2687 bytes
DetailTemplateJson = {'NO_INDEX':{'sql':"SELECT\n     OWNER = DB_NAME() + '.' + SCHEMA_NAME(o.schema_id)\n    ,TABLE_NAME = o.NAME\nFROM sys.objects o\nINNER JOIN sys.indexes i ON i.OBJECT_ID = o.OBJECT_ID\n-- tables that are heaps without any nonclustered indexes\nWHERE (\n        o.type = 'U'\n        AND o.OBJECT_ID NOT IN (\n            SELECT OBJECT_ID\n            FROM sys.indexes\n            WHERE index_id > 0\n            )\n        )", 
  'schema_name':''}, 
 'TABLE_OLD_STATS':{'sql': "\nSELECT DISTINCT\n  DB_NAME() + '.' + schema_name(schema_id) as [OWNER],\n  OBJECT_NAME(s.[object_id]) AS [TABLE_NAME],\n  c.name AS ColumnName,\n  s.name AS StatName,\n  STATS_DATE(s.[object_id], s.stats_id) AS LastUpdated,\n  DATEDIFF(d,STATS_DATE(s.[object_id], s.stats_id),getdate()) as [MESSAGE],\n  s.auto_created,\n  s.user_created,\n  s.no_recompute\nFROM sys.stats s\nJOIN sys.stats_columns sc\nON sc.[object_id] = s.[object_id] AND sc.stats_id = s.stats_id\nJOIN sys.columns c ON c.[object_id] = sc.[object_id] AND c.column_id = sc.column_id\nJOIN sys.partitions par ON par.[object_id] = s.[object_id]\nJOIN sys.objects obj ON par.[object_id] = obj.[object_id]\nWHERE OBJECTPROPERTY(s.OBJECT_ID,'IsUserTable') = 1\nAND (s.auto_created = 1 OR s.user_created = 1)\nAND DATEDIFF(d,STATS_DATE(s.[object_id], s.stats_id),getdate()) > {pred}\nORDER BY MESSAGE desc"}, 
 'MISSING_INDEX':{'sql': "\n    select\n    db_name(mid.database_id) + '.' + schema_name(t.schema_id) as [OWNER],\n    t.NAME AS TABLE_NAME,\n    migs.user_seeks,\n    migs.user_scans,\n    convert(char,migs.last_user_seek,120),\n    convert(char,migs.last_user_scan,120),\n    migs.avg_total_user_cost,\n    migs.avg_user_impact,\n    equality_columns,\n    inequality_columns,\n    included_columns\nFROM sys.dm_db_missing_index_details AS mid\nINNER JOIN sys.tables t ON t.OBJECT_ID = mid.object_id\nINNER JOIN sys.dm_db_missing_index_groups AS mig\nON mig.index_handle = mid.index_handle\nINNER JOIN sys.dm_db_missing_index_group_stats  AS migs\nON mig.index_group_handle=migs.group_handle\nORDER BY mig.index_group_handle, mig.index_handle\n"}, 
 'INDEX_COLUMNS':{'sql': "\nSELECT\n    DB_NAME() + '.' + schema_name(s.schema_id) as [OWNER],\n    t.name as [TABLE_NAME],\n    INDEX_NAME = ind.name,\n    count(*) as [MESSAGE]\nFROM\n    sys.indexes ind\nINNER JOIN\n    sys.index_columns ic ON  ind.object_id = ic.object_id and ind.index_id = ic.index_id\nINNER JOIN\n    sys.columns col ON ic.object_id = col.object_id and ic.column_id = col.column_id\nINNER JOIN\n    sys.tables t ON ind.object_id = t.object_id\nLEFT OUTER JOIN\n    sys.schemas s ON t.schema_id = s.schema_id\ngroup by s.schema_id,t.name,ind.name\nhaving count(*) > {pred}\n"}}
# okay decompiling ./restful/hawkeye/sqlaudit/enum/sqlserver_detail_template_enum.pyc