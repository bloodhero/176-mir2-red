# -*- coding: gb18030 -*-
import re
from multidict import MultiDict
# ../../Mir200/Envir/MonGen.txt，读取其中的怪物数据
monster_data = MultiDict()
with open('../../Mir200/Envir/MonGen.txt', 'r', encoding='gb18030') as f:
    lines = f.readlines()

    for index, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        parts = re.match(r';(\w*)$', line)
        if parts and index + 2 < len(lines):
            ditu_line = lines[index + 2].strip()
            ditu_parts = re.fullmatch(r'^(\w*)[\s\t]*\d*[\s\t]*\d*[\s\t]*\w*[\s\t]*\d*[\s\t]*\d*[\s\t]*\d*$', ditu_line)
            if ditu_parts and len(ditu_parts.groups()) > 0 and ditu_parts.group(1) != '':
                monster_data.add(parts.group(1), ditu_parts.group(1))  # 使用 MultiDict 存储数据

print(monster_data)  # For debugging purposes

# 持久化到文件
with open('monster_data.txt', 'w', encoding='gb18030') as f:
    for key, value in monster_data.items():
        f.write(f'{key}: {value}\n')