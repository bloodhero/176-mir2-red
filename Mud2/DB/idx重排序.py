# -*- coding: utf-8 -*-
import sqlite3

db_path = 'REDM2.DB'  # 替换为你的数据库文件路径
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# 1. 查询所有数据，按原 Idx 排序
cur.execute("SELECT * FROM stditems ORDER BY Idx")
rows = cur.fetchall()

# 2. 获取字段名
cur.execute("PRAGMA table_info(stditems)")
columns = [row[1] for row in cur.fetchall()]
idx_index = columns.index('Idx')

# 3. 依次更新 Idx 字段
for new_idx, row in enumerate(rows):
    pk_value = row[idx_index]  # 原主键值
    # 构造 SET 语句
    cur.execute("UPDATE stditems SET Idx=? WHERE Idx=?", (new_idx, pk_value))

conn.commit()
conn.close()
print("Idx 字段已从0开始递增更新。")