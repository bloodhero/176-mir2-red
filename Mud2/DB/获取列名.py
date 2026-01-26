import sqlite3
print("获取表t的所有字段名")
conn = sqlite3.connect('./REDM2.DB')
cursor = conn.execute("PRAGMA table_info(stditems)")
column_names = [info[1] for info in cursor.fetchall()]
field_list = ', '.join(column_names)
print(field_list)