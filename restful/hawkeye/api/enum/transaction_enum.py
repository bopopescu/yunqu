# uncompyle6 version 3.2.3
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.5 (default, Jul 13 2018, 13:06:57) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)]
# Embedded file name: ./api/enum/transaction_enum.py
# Compiled at: 2018-08-23 19:33:14
# Size of source mod 2**32: 3948 bytes
from enum import Enum

class Transaction_Query(Enum):
    oracle = "\n            select\n                vs.sid || ','|| vs.serial# || '@' || vs.inst_id as SESSION_ID,\n                vs.username,\n                vs.machine,\n                vs.sql_id,\n                vs.event,\n                vt.status,\n                vt.xidusn || ',' ||vt.xidslot || ',' || vt.xidsqn xid,\n                to_char(vt.start_date,'yyyy-mm-dd hh24:mi:ss') TRX_STARTED,\n                vt.log_io,\n                vt.phy_io,\n                vt.used_ublk,\n                vt.used_urec,\n                vs.inst_id,\n                round((sysdate-vt.start_date)*24*3600) TRX_SECONDS\n            from\n            gv$transaction vt,\n            gv$session vs\n            where   vt.addr = vs.taddr\n            and     vt.inst_id = vs.inst_id\n            order by vt.used_ublk desc"
    db2 = "\n    SELECT\n    APPLICATION_HANDLE as SESSION_ID,\n    APPLICATION_ID,\n    SESSION_AUTH_ID,\n    uow_id,\n    to_char(UOW_START_TIME,'yyyy-mm-dd hh24:mi:ss') TRX_STARTED,\n    timestampdiff(2,char(CURRENT_TIMESTAMP - UOW_START_TIME)) TRX_SECONDS,\n    SUBSTR(APPLICATION_ID, 1, INSTR(APPLICATION_ID,'.') -1) as MACHINE,\n    CLIENT_USERID,\n    UOW_LOG_SPACE_USED,\n    TOTAL_CPU_TIME/1000000 TOTAL_CPU_TIME,\n    POOL_DATA_L_READS + POOL_TEMP_DATA_L_READS +  POOL_XDA_L_READS + POOL_TEMP_XDA_L_READS +  POOL_INDEX_L_READS + POOL_TEMP_INDEX_L_READS AS POOL_L_READS,\n    POOL_DATA_P_READS + POOL_TEMP_DATA_P_READS +  POOL_XDA_P_READS + POOL_TEMP_XDA_P_READS +  POOL_INDEX_P_READS + POOL_TEMP_INDEX_P_READS AS POOL_P_READS\nFROM TABLE(MON_GET_UNIT_OF_WORK(NULL,-2))\nwhere UOW_START_TIME is not null\nand UOW_LOG_SPACE_USED > 0"
    mysql = "\n    select\n        trx_id,\n        trx_state,\n        DATE_FORMAT(trx_started, '%Y-%m-%d %T') TRX_STARTED,\n        trx_requested_lock_id,\n        DATE_FORMAT(trx_wait_started, '%Y-%m-%d %T') TRX_WAIT_STARTED,\n        trx_mysql_thread_id as SESSION_ID,\n        trx_query,\n        trx_operation_state,\n        trx_tables_in_use,\n        trx_tables_locked,\n        trx_rows_locked,\n        TRX_ROWS_MODIFIED,\n        trx_isolation_level,\n        TIMESTAMPDIFF(SECOND, trx_started, CURRENT_TIMESTAMP) AS TRX_SECONDS,\n        (select host from information_schema.processlist p where p.id = trx.trx_mysql_thread_id) as MACHINE\nfrom information_schema.innodb_trx trx"
    sqlserver = '\n                        SELECT\n            [s_tst].[SESSION_ID],\n            [s_es].[login_name] AS [LOGIN_NAME],\n            [s_es].[status] AS [STATUS],\n            [s_es].[HOST_NAME] as [MACHINE],\n            DB_NAME (s_tdt.database_id) AS [Database],\n            CONVERT(varchar(25), [s_tdt].[database_transaction_begin_time], 120) AS [TRX_STARTED],\n            [s_tdt].[database_transaction_log_bytes_used] AS [LOG_BYTES],\n            [s_tdt].[database_transaction_log_bytes_reserved] AS [LOG_RSVD],\n            s_est.TEXT AS [SQL_TEXT],\n            substring(sys.fn_sqlvarbasetostr(s_ec.most_recent_sql_handle),3,1000) SQL_ID,\n            DATEDIFF(SECOND, [s_tdt].[database_transaction_begin_time], getdate()) TRX_SECONDS\n        FROM\n            sys.dm_tran_database_transactions [s_tdt]\n        JOIN\n            sys.dm_tran_session_transactions [s_tst]\n        ON\n            [s_tst].[transaction_id] = [s_tdt].[transaction_id]\n        JOIN\n            sys.[dm_exec_sessions] [s_es]\n        ON\n            [s_es].[session_id] = [s_tst].[session_id]\n        JOIN\n            sys.dm_exec_connections [s_ec]\n        ON\n            [s_ec].[session_id] = [s_tst].[session_id]\n        CROSS APPLY\n            sys.dm_exec_sql_text ([s_ec].[most_recent_sql_handle]) AS [s_est]\n        where\n            s_tdt.database_transaction_begin_time is not null\n        ORDER BY\n            [TRX_STARTED] ASC'


Local_Transaction_Query = "\nselect\n    transactions\nfrom\n    monitor_transaction\nwhere database_id = '{}' and\n    created_at = to_timestamp({})"
# okay decompiling ./restful/hawkeye/api/enum/transaction_enum.pyc
