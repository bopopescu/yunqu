# uncompyle6 version 3.2.3
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.5 (default, Jul 13 2018, 13:06:57) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)]
# Embedded file name: ./api/enum/space_enum.py
# Compiled at: 2018-08-23 19:33:14
# Size of source mod 2**32: 11526 bytes
Space_Query = {'oracle':"SELECT a.tablespace_name,\n       Round(( total - free ) / maxsize * 100, 1) USED_PCT,\n       b.autoextensible,\n       total total_mb,\n       ( total - free ) USED,\n       free,\n       b.cnt DATAFILE_COUNT,\n       c.status,\n       c.CONTENTS,\n       c.extent_management,\n       c.allocation_type,\n       b.maxsize\nFROM   (SELECT tablespace_name,\n               Round(SUM(bytes) / ( 1024 * 1024 ), 1) free\n        FROM   dba_free_space\n        GROUP  BY tablespace_name) a,\n       (SELECT tablespace_name,\n               Round(SUM(bytes) / ( 1024 * 1024 ), 1) total,\n               Count(*)                               cnt,\n               Max(autoextensible)                  autoextensible,\n               sum(decode(autoextensible, 'YES', floor(maxbytes/1048576), floor(bytes / 1048576 ))) maxsize\n        FROM   dba_data_files\n        GROUP  BY tablespace_name) b,\n       dba_tablespaces c\nWHERE  a.tablespace_name = b.tablespace_name\n       AND a.tablespace_name = c.tablespace_name\nUNION ALL\nSELECT /*+ NO_MERGE */ a.tablespace_name,\n                       Round(100 * ( B.tot_gbbytes_used / A.maxsize ), 1) PERC_USED,\n                       a.aet,\n                       Round(A.avail_size_gb, 1),\n                       Round(B.tot_gbbytes_used, 1),\n                       ( Round(A.avail_size_gb, 1) - Round(B.tot_gbbytes_used, 1) ),\n                       a.cnt DATAFILE_COUNT,\n                       c.status,\n                       c.CONTENTS,\n                       c.extent_management,\n                       c.allocation_type,\n                       a.maxsize\nFROM   (SELECT tablespace_name,\n               SUM(bytes) / Power(2, 20) AVAIL_SIZE_GB,\n               Max(autoextensible)       aet,\n               Count(*)                  cnt,\n               sum(decode(autoextensible, 'YES', floor(maxbytes/1048576), floor(bytes/1048576))) maxsize\n        FROM   dba_temp_files\n        GROUP  BY tablespace_name) A,\n       (SELECT tablespace_name,\n               SUM(bytes_used) / Power(2, 20) TOT_GBBYTES_USED\n        FROM   gv$temp_extent_pool\n        GROUP  BY tablespace_name) B,\n       dba_tablespaces c\nWHERE  a.tablespace_name = b.tablespace_name\n       AND a.tablespace_name = c.tablespace_name", 
 'db2':'\n    select tbsp_name tablespace_name, tbsp_type as Type, tbsp_state as STATUS,\n      round(cast(tbsp_total_size_kb as FLOAT) / 1024 ,2) TOTAL_MB,\n      round(cast(tbsp_used_size_kb as FLOAT) / 1024 ,2) USED,\n      round(cast(tbsp_free_size_kb as FLOAT) / 1024 ,2) FREE,\n      tbsp_utilization_percent USED_PCT\n    from sysibmadm.tbsp_utilization\n    ', 
 'mysql':'\n        SELECT TABLE_SCHEMA as TABLESPACE_NAME,\n        cast(floor(sum( data_length + index_length + data_free )/1024/1024) as UNSIGNED) TOTAL_MB,\n        cast(floor(sum( data_length + index_length)/1024/1024) as UNSIGNED) USED,\n        cast(floor(sum( data_free )/1024/1024) as UNSIGNED) FREE,\n        cast(floor(sum( data_length)/1024/1024) as UNSIGNED) TABLE_SIZE_MB,\n        cast(floor(sum( index_length)/1024/1024) as UNSIGNED) INDEX_SIZE_MB\n        FROM information_schema.TABLES\n        group by table_schema\n    ', 
 'sqlserver':'\n            SELECT DB_NAME(mf.database_id) TABLESPACE_NAME,\n            sum(size)*8/1024 USED,\n            sum(size)*8/1024 TOTAL_MB\n        FROM sys.master_files mf\n        where type = 0\n            group by mf.database_id'}
Space_Realtime_Query = {'oracle': {'diskgroup':'\n    SELECT\n        GROUP_NUMBER,\n        NAME,\n        ALLOCATION_UNIT_SIZE/1024/1024 AU_SIZE_MB,\n        STATE,\n        TYPE,\n        round((TOTAL_MB-FREE_MB)/TOTAL_MB*100) USED_PCT,\n        trunc(TOTAL_MB/1024) TOTAL_GB,\n        trunc(FREE_MB/1024) FREE_GB,\n        trunc(USABLE_FILE_MB/1024) USABLE_FILE_GB,\n        trunc(REQUIRED_MIRROR_FREE_MB/1024) REQUIRED_MIRROR_FREE_GB\n    FROM\n        V$ASM_DISKGROUP', 
            'switch_trend':"\n        SELECT (trunc(first_time, 'HH24') - to_date('1970-01-01','YYYY-MM-DD')) * 60 * 60 * 24 * 1000 TIME, count(*) COUNT\nFROM gv$log_history\nwhere first_time > trunc(sysdate, 'HH24') - {days}\nGROUP by trunc(first_time,'HH24')\nORDER BY trunc(first_time,'HH24')", 
            'redo':'\n    SELECT  V1.GROUP#,\n            V1.THREAD#,\n            SEQUENCE#,\n            FIRST_CHANGE#,\n            V1.STATUS,\n            V1.ARCHIVED,\n            V1.BYTES/1048576 SIZE_MB,\n            MEMBER\n    FROM V$LOG V1, V$LOGFILE V2\n    WHERE V1.GROUP# = V2.GROUP#\n    ORDER BY 1', 
            'control':'select\n    INST_ID,\n    STATUS,\n    NAME,\n    IS_RECOVERY_DEST_FILE,\n    BLOCK_SIZE,\n    FILE_SIZE_BLKS\nfrom\n    gv$controlfile\norder by inst_id'}}
Space_Detail_Lag_Query = "select extract(epoch from created_at)*1000 created_at, delta\n    from\n    (\n     select created_at, used - lag(used) over (order by created_at) delta\n     from monitor_space where database_id = '{pk}' and name = '{name}' and created_at > TIMESTAMP 'now' - interval '{days} days'\n     order by created_at\n     ) a where delta is not null"
Space_Detail_Realtime_Query = {'oracle':{'segment':"select * from (\n            select\n                owner,\n                segment_name,\n                partition_name,\n                segment_type,\n                round(bytes/1048576) SIZE_MB,\n                extents\n            from dba_segments\n            where tablespace_name = '{name}'\n            order by bytes desc\n        ) where rownum < {limit}", 
  'datafile':"\nselect\n    file_id,\n    file_name,\n    autoextensible,\n    round(bytes/1048576,2) SIZE_MB,\n    decode(autoextensible, 'YES', round(maxbytes/1048576,2), null) MAXSIZE\nFrom\n    (select tablespace_name, file_id, file_name, autoextensible, bytes, maxbytes from dba_data_files where tablespace_name = '{name}'\n     union all\n     select tablespace_name, file_id, file_name, autoextensible, bytes, maxbytes from dba_temp_files where tablespace_name = '{name}'\n    )\norder by\n    file_name", 
  'temp':"\n        SELECT   S.sid || ',' || S.serial# || ',@'|| S.inst_id session_id, S.username, S.osuser, P.spid, S.module,\n         P.program, SUM (T.blocks) * TBS.block_size / 1024 / 1024 used, T.tablespace,\n         COUNT(*) statements\nFROM     gv$sort_usage T, gv$session S, dba_tablespaces TBS, gv$process P\nWHERE    T.session_addr = S.saddr\nAND      S.paddr = P.addr\nAND      T.tablespace = TBS.tablespace_name\nGROUP BY S.sid, S.serial#, S.inst_id, S.username, S.osuser, P.spid, S.module,\n         P.program, TBS.block_size, T.tablespace\nORDER BY SUM(T.blocks)"}, 
 'db2':{'segment':"\n        select tabschema OWNER, tabname TABLE_NAME, TYPE, npages from SYScat.tables where tbspace ='{name}'\n        order by npages desc fetch first {limit} rows only\n        ", 
  'datafile':"\nSELECT container_name, TOTAL_PAGES, PAGES_READ, PAGES_WRITTEN,\n       round(fs_used_size/1024/1024/1024) as FS_USED,\n       round(fs_total_size/1024/1024/1024) as FS_TOTAL,\n       CASE WHEN fs_total_size > 0\n            THEN DEC(100*(FLOAT(fs_used_size)/FLOAT(fs_total_size)),5,2)\n            ELSE DEC(-1,5,2)\n       END as USED_PCT\nFROM TABLE(MON_GET_CONTAINER('',-1)) AS t\nwhere TBSP_NAME ='{name}'\nORDER BY USED_PCT DESC", 
  'temp':'\nselect STMT_TEXT,\n    decimal(total_section_sort_time/num_executions/1000000,22,2) as TOTAL_SECTION_SORT_TIME,\n    TOTAL_SORTS/num_executions as "TOTAL_SORTS",\n    POST_THRESHOLD_SORTS/num_executions "POST_THRESHOLD_SORTS",\n    POST_SHRTHRESHOLD_SORTS/num_executions "POST_SHRTHRESHOLD_SORTS",\n    SORT_OVERFLOWS/num_executions "SORT_OVERFLOWS"\nfrom TABLE (MON_GET_PKG_CACHE_STMT(null, null, null, -1)) AS tf\nwhere num_executions>0 and total_section_sort_time > 0\norder by total_section_sort_time/num_executions desc\nfetch first {limit} rows only'}, 
 'mysql':{'segment': "\n    SELECT TABLE_SCHEMA OWNER,\n        TABLE_NAME,\n        cast(floor(data_length )/1024/1024 as UNSIGNED) TABLE_SIZE_MB,\n        cast(floor(index_length )/1024/1024 as UNSIGNED) INDEX_SIZE_MB,\n        cast(floor(data_free )/1024/1024 as UNSIGNED) FREE,\n        TABLE_ROWS,\n        AVG_ROW_LENGTH,\n        CREATE_TIME,\n        TABLE_Collation,\n        ENGINE,\n        ROW_FORMAT\n        FROM information_schema.TABLES\n        where TABLE_SCHEMA = '{name}'\n        order by data_length desc"}, 
 'sqlserver':{'segment':'\n                SELECT top {limit}\n            t.NAME AS Table_Name,\n            i.name as index_Name,\n            sum(p.rows) as RowCounts,\n            sum(a.total_pages) as TotalPages,\n            (sum(a.total_pages) * 8) / 1024 as SIZE_MB\n        FROM\n            sys.tables t\n        INNER JOIN\n            sys.indexes i ON t.OBJECT_ID = i.object_id\n        INNER JOIN\n            sys.partitions p ON i.object_id = p.OBJECT_ID AND i.index_id = p.index_id\n        INNER JOIN\n            sys.allocation_units a ON p.partition_id = a.container_id\n        WHERE\n            i.OBJECT_ID > 255 AND\n            i.index_id <= 1\n        GROUP BY\n            t.NAME, i.object_id, i.index_id, i.name\n        ORDER BY\n            SUM(a.total_pages) DESC\n        ', 
  'datafile':"\n                SELECT mf.physical_name FILE_NAME,\n                size*8/1024 TOTAL_MB\n        FROM sys.master_files mf\n        where type = 0 and DB_NAME(mf.database_id) = '{name}'\n        "}}
Space_Total_Lag_Query = "select extract(epoch from created_at)*1000 created_at, delta\nfrom\n(\n select created_at, used - lag(used) over (order by created_at) delta\n from\n(\nselect created_at, sum(used) used\nfrom monitor_space where database_id = '{pk}' and created_at > TIMESTAMP 'now' - interval '{days} days'\nand (type is null or type = 'PERMANENT')\ngroup by created_at\n) a\norder by created_at\n) b where delta is not null"
Space_Total_Query = "\n select round(sum(total_mb)/1024) total_gb, round(sum(used)/1024) used_gb, round(sum(free)/1024) free_gb,\n        round(sum(used) / case when sum(total_mb) > 0 then sum(total_mb) else 1 end * 100) used_pct,\n        count(*) tablespace_count,\n        to_char(created_at, 'YYYY-MM-DD HH24:MI:SS') sample_time\n from monitor_space where database_id = '{pk}' and created_at = (select max(created_at) from monitor_space where database_id = '{pk}')\n group by created_at\n order by created_at desc limit 1"
SQLServer_Space_Total_Query = "\n select round(sum(total_mb)/1024) total_gb, --round(sum(used)/1024) used_gb, round(sum(free)/1024) free_gb,\n        --round(sum(used) / case when sum(total_mb) > 0 then sum(total_mb) else 1 end * 100) used_pct,\n        count(*) tablespace_count,\n        to_char(created_at, 'YYYY-MM-DD HH24:MI:SS') sample_time\n from monitor_space where database_id = '{pk}' and created_at = (select max(created_at) from monitor_space where database_id = '{pk}')\n group by created_at\n order by created_at desc limit 1"

def reprocess_query(queires, options):
    if isinstance(queires, dict):
        new_dict = {}
        for k, v in queires.items():
            new_dict[k] = v.format(**options)

        return new_dict
    else:
        queires = queires.format(**options)
        return queires


def is_temp(db_type, name_detail):
    if db_type == 'db2':
        import re
        prog = re.compile('TEMP', re.IGNORECASE)
        result = prog.search(name_detail.get('TABLESPACE_NAME'))
        if result:
            return True
        return False
    else:
        if db_type == 'oracle':
            return name_detail.get('CONTENTS') == 'TEMPORARY'
# okay decompiling ./restful/hawkeye/api/enum/space_enum.pyc