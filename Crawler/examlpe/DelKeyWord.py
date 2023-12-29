def remove_keyword(filepath, keyword):
    """逐行检查文件并删除包含指定关键字的行"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
 
    with open(filepath, 'w', encoding='utf-8') as f:
        for line in lines:
            if keyword not in line:
                f.write(line)
 
def remove_multi(file_path):
    # 读取文件内容到列表
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
 
    # 使用set去重
    lines_set = set(lines)
 
    # 将去重后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines_set)
 
    print(f'{len(lines) - len(lines_set)} 个重复行被删除')
