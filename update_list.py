import os
import json

# 配置
base_dir = 'images'
categories = ['landscape', 'portrait'] # 两个分类
exts = ['.jpg', '.png', '.jpeg', '.gif', '.webp']

for cat in categories:
    cat_path = os.path.join(base_dir, cat)
    
    # 如果文件夹不存在就创建一个，防止报错
    if not os.path.exists(cat_path):
        os.makedirs(cat_path)
        
    # 获取该分类下的所有图片
    files = [f for f in os.listdir(cat_path) if any(f.lower().endswith(e) for e in exts)]
    
    # 写入对应的 JSON 文件 (如 landscape.json)
    with open(f'{cat}.json', 'w', encoding='utf-8') as f:
        json.dump(files, f)

print("横屏和竖屏清单已同步更新！")
