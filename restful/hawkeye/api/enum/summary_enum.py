# uncompyle6 version 3.2.3
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.5 (default, Jul 13 2018, 13:06:57) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)]
# Embedded file name: ./api/enum/summary_enum.py
# Compiled at: 2018-08-23 19:33:14
# Size of source mod 2**32: 7089 bytes
from api.enum.database_enum import DatabaseType
SummaryQuery = {'oracle':{'database':"select name, (select count(*) from gv$instance) inst_cnt,\n                      (SELECT version platform FROM PRODUCT_COMPONENT_VERSION where product like 'Oracle%') VERSION,\n         log_mode, open_mode, DATABASE_ROLE, FORCE_LOGGING, FLASHBACK_ON from v$database", 
  'memory':"select\n  gi.instance_number inst_id,\n  (select round(bytes/1073741824,1) from gv$sgainfo where inst_id = gi.instance_number and NAME='Maximum SGA Size') Maximum_SGA,\n  (select round(bytes/1073741824,1) from gv$sgainfo where inst_id = gi.instance_number and NAME='Free SGA Memory Available') FREE_SGA,\n  (select round(bytes/1073741824,1) from gv$sgainfo where inst_id = gi.instance_number and NAME='Redo Buffers') REDO_BUFFER,\n  (select round(bytes/1073741824,1) from gv$sgainfo where inst_id = gi.instance_number and NAME='Buffer Cache Size') BUFFER_CACHE,\n  (select round(bytes/1073741824,1) from gv$sgainfo where inst_id = gi.instance_number and NAME='Shared Pool Size') SHARED_POOL\nfrom gv$instance gi", 
  'instance':"select instance_number inst_id,instance_name,host_name,to_char(startup_time,'yyyy-mm-dd hh24:mi:ss') startup_time, status from gv$instance order by instance_number", 
  'backup':"\nselect SESSION_KEY, INPUT_TYPE, STATUS, START_TIME, END_TIME, HOURS\nfrom\n(\n    SELECT SESSION_KEY, INPUT_TYPE, STATUS,\n           TO_CHAR(START_TIME,'mm/dd/yy hh24:mi') START_TIME,\n           TO_CHAR(END_TIME,'mm/dd/yy hh24:mi')   END_TIME,\n           round(ELAPSED_SECONDS/3600,1)          HOURS\n    FROM V$RMAN_BACKUP_JOB_DETAILS\n    where INPUT_TYPE in ('DB INCR','DB FULL')\n    ORDER BY SESSION_KEY desc)\nwhere rownum = 1", 
  'parameter':"\n            with numinst as\n       (\n         select count(distinct inst_id) cnt from gv$instance\n       ),\n       pval1e as\n       (\n         select name, INST_ID\n           from\n         (\n            select name, INST_ID\n              from gv$parameter\n             where  isdefault = 'FALSE'\n             group by name, inst_id\n    --          having count(*) > 1\n         )\n       ),\n       pval as\n       (\n         select e.name\n              , e.inst_id\n              , b.value bval\n              , decode(b.value, e.value, NULL, e.value) eval\n              , count(*)   instcnt\n           from gv$parameter b,\n                gv$parameter e\n         where\n            b.inst_id(+) = e.inst_id\n            and b.name(+)  = e.name\n    --        and b.hash(+)  = e.hash\n            and b.value(+)           = e.value\n    --        and e.name not like '\\_\\_%' escape ''\n            and e.name in (select name from pval1e)\n            and (   nvl(b.isdefault, 'X')   = 'FALSE'\n                 or nvl(b.ismodified,'X')  <> 'FALSE'\n                 or     e.ismodified       <> 'FALSE'\n                 or nvl(e.value,0)         <> nvl(b.value,0)\n                )\n            and ( b.value is not null or e.value is not null )\n         group by e.name\n                  , b.value\n                  , decode(b.value, e.value, NULL, e.value)\n                  , rollup(e.inst_id)\n       ),\n     pval2 as ( select /*+ NO_MERGE(numinst) */\n                  name\n                  ,'  *'             inst_id\n                  , decode( bval, NULL, '(NULL)', bval) bvalue\n                  , nvl(eval, '  ') evalue\n                from pval , numinst\n                where inst_id is null and bval is not null\n                  and instcnt = numinst.cnt\n                union all\n                select /* get parameters that are not the same for all instances */\n                  name\n                  , lpad(to_char(inst_id),3)  inst_id\n                  , decode( bval, NULL, '(NULL)', bval) bvalue\n                  , nvl(eval, '  ') evalue\n                from pval , numinst\n                where inst_id is not null and bval is null\n                  and instcnt < numinst.cnt\n              )\n    select name, inst_id, bvalue value\n     from pval2\n     order by name, inst_id\n             , concat(decode(bvalue, '(NULL)', NULL, bvalue), evalue)"}, 
 'mysql':{'database':"\nshow global variables where Variable_name in ('version','version_comment','version_compile_machine','version_compile_os','query_cache_size','thread_cache_size','innodb_buffer_pool_size','query_cache_size','thread_cache_size','table_cache','general_log','log_bin','log_slow_queries','slow_query_log','default_storage_engine','max_connections','key_buffer_size','join_buffer_size','sort_buffer_size');        ", 
  'status':"\nshow global status where Variable_name in ('Com_select','Com_insert','Com_update','Com_delete','Max_used_connections','Threads_connected')\n        "}, 
 'sqlserver':{'parameter':'\nselect name,\n    convert(int, minimum) as minimum,\n    convert(int, maximum) as maximum,\n  convert(int, isnull(value, value_in_use)) as config_value,\n    convert(int, value_in_use) as run_value,\n    is_dynamic,\n    description\nfrom sys.configurations\norder by name', 
  'database':'\n        select @@version as [VERSION]'}, 
 'db2':{'database':"\n          SELECT\n        b.INST_NAME INSTANCE_NAME,\n        to_char(a.DB2START_TIME,'yyyy-mm-dd hh24:mi:ss') START_TIME,\n        a.PRODUCT_NAME VERSION,\n        a.SERVICE_LEVEL,\n        b.FIXPACK_NUM,\n        a.DB2_STATUS STATUS,\n        c.total_size TOTAL_MB,\n        d.appls_cur_cons\n    from\n        SYSIBMADM.SNAPDBM a,\n        SYSIBMADM.ENV_INST_INFO b,\n        (select sum(tbsp_total_size_kb / 1024 ) total_size from sysibmadm.tbsp_utilization) c,\n        (select * from sysibmadm.snapdb) d", 
  'parameter':'\n        SELECT\n        DBPARTITIONNUM AS MEMBER,\n        NAME,\n        VALUE,\n        VALUE_FLAGS,\n        DEFERRED_VALUE,\n        DEFERRED_VALUE_FLAGS\n    FROM\n        SYSIBMADM.DBCFG WITH UR', 
  'instance':'\n            SELECT\n        MAX(MEMBER) as MEMBER,\n        HOST_NAME,\n        max(OS_NAME) as OS_NAME,\n        MAX(CPU_TOTAL) as CPU_TOTAL,\n        MAX(MEMORY_TOTAL) as MEMORY_TOTAL,\n        MAX(MEMORY_FREE) as MEMORY_FREE,\n        MAX(MEMORY_SWAP_TOTAL) as MEMORY_SWAP_TOTAL,\n        MAX( MEMORY_SWAP_FREE) as MEMORY_SWAP_FREE\n    from\n        table(SYSPROC.ENV_GET_SYSTEM_RESOURCES())\n    group by\n        HOST_NAME WITH UR'}}
# okay decompiling ./restful/hawkeye/api/enum/summary_enum.pyc