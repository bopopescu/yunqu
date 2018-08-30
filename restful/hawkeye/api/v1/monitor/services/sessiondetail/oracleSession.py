# uncompyle6 version 3.2.3
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.5 (default, Jul 13 2018, 13:06:57) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)]
# Embedded file name: ./api/v1/monitor/services/sessiondetail/oracleSession.py
# Compiled at: 2018-08-23 19:33:14
# Size of source mod 2**32: 3890 bytes
Detai_Query = "\n        select\n        --  server 0-6\n            s.sid,\n            s.serial#,\n            s.status,\n            s.username,\n            p.spid,\n            to_char(s.logon_time,'YYYY-MM-DD HH24:MI:SS') logon_time,\n            server,\n        --  client 7-10\n            s.osuser,\n            s.process,\n            s.machine,\n            utl_inaddr.get_host_address(s.machine) IP,\n        --    'UNKNOWN' IP,\n        --  application 11-17\n            s.sql_id,\n            s.prev_sql_id,\n            s.last_call_et,\n            s.program,\n            s.module,\n            s.action,\n            s.service_name,\n        --  event 18-23\n            event,\n            wait_class,\n            p1,\n            p2,\n            p3,\n            SECONDS_IN_WAIT,\n        --  blocking session 24 - 25\n            blocking_instance,\n            blocking_session,\n        --  transaction 26 - 31\n            t.xidusn,\n            t.xidslot,\n            t.xidsqn,\n            to_char(T.start_date,'yyyy-mm-dd hh24:mi:ss') TRX_STARTED,\n            t.used_ublk,\n            t.used_urec\n        from\n            gv$session s,\n            gv$process P,\n            gv$transaction T\n        where\n          S.paddr = P.addr\n          and s.taddr = T.addr(+)\n          and s.inst_id = {inst_id}\n          and s.sid = {sid}\n          and s.serial# = {serial}"
Detai_Query_Without_IP = "\n        select\n        --  server 0-6\n            s.sid,\n            s.serial#,\n            s.status,\n            s.username,\n            p.spid,\n            to_char(s.logon_time,'YYYY-MON-DD HH24:MI:SS') logon_time,\n            server,\n        --  client 7-10\n            s.osuser,\n            s.process,\n            s.machine,\n        --    utl_inaddr.get_host_address(s.machine) IP,\n            'UNKNOWN' IP,\n        --  application 11-17\n            s.sql_id,\n            s.prev_sql_id,\n            s.last_call_et,\n            s.program,\n            s.module,\n            s.action,\n            s.service_name,\n        --  event 18-23\n            event,\n            wait_class,\n            p1,\n            p2,\n            p3,\n            SECONDS_IN_WAIT,\n        --  blocking session 24 - 25\n            blocking_instance,\n            blocking_session,\n        --  transaction 26 - 31\n            t.xidusn,\n            t.xidslot,\n            t.xidsqn,\n            to_char(T.start_date,'yyyy-mm-dd hh24:mi:ss') TRX_STARTED,\n            t.used_ublk,\n            t.used_urec\n        from\n            gv$session s,\n            gv$process P,\n            gv$transaction T\n        where\n          S.paddr = P.addr\n          and s.taddr = T.addr(+)\n          and s.inst_id = {inst_id}\n          and s.sid = {sid}\n          and s.serial# = {serial}"
Old_Cursor_Query = '\n    select\n    sql_id, sql_text, count(*) count,\n    (select  trunc(elapsed_time/decode(executions,0,1,executions)/1000) from v$sqlarea sa where  sa.sql_id = s.sql_id and rownum = 1) ELAPSED_TIME_PER_EXECUTION,\n    (select  trunc(buffer_gets/decode(executions,0,1,executions)) from v$sqlarea sa where sa.sql_id = s.sql_id and rownum = 1) BUFFER_GETS_PER_EXECUTION\n    from gv$open_cursor s\n    where s.inst_id = {inst_id} and s.sid = {sid}\n    group by inst_id, sql_id, sql_text\n    order by count(*) desc\n    '
New_Cursor_Query = "\n    select\n    sql_id, sql_text, count(*) count, to_char(max(LAST_SQL_ACTIVE_TIME),'YYYY-MM-DD HH24:MI:SS') LAST_SQL_ACTIVE_TIME,\n    (select  trunc(elapsed_time/decode(executions,0,1,executions)/1000) from v$sqlarea sa where sa.sql_id = s.sql_id and rownum = 1) ELAPSED_TIME_PER_EXECUTION,\n    (select  trunc(buffer_gets/decode(executions,0,1,executions)) from v$sqlarea sa where sa.sql_id = s.sql_id and rownum = 1) BUFFER_GETS_PER_EXECUTION\n    from gv$open_cursor s\n    where s.inst_id = {inst_id} and s.sid = {sid}\n    group by inst_id, sql_id, sql_text\n    order by count(*) desc\n"
# okay decompiling ./restful/hawkeye/api/v1/monitor/services/sessiondetail/oracleSession.pyc
