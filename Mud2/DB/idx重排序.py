# -*- coding: utf-8 -*-
import sqlite3

db_path = 'REDM2.DB'  # 替换为你的数据库文件路径
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# 将数据库中的stditems表的Idx字段重新排序，idx有重复的情况
print("开始重新排序stditems表的Idx字段...")
cur.execute("SELECT Idx, Name FROM StdItems")
rows = cur.fetchall()
new_idx = 0
for row in rows:
    name  = row[1]
    cur.execute("UPDATE StdItems SET Idx = ? WHERE Name = ?", (new_idx, name))
    new_idx += 1
conn.commit()
conn.close()
print("Idx 字段已从0开始递增更新。")