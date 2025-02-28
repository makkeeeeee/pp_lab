import re

def parse_receipt(text):
    # 正则表达式：匹配商品名称和价格
    pattern = r'(\w+)\s+价格:\s+(\d+\.\d{2})'
    return re.findall(pattern, text)

# 读取文件内容
with open('/Users/mariyaerzhan/Desktop/pp2/PP2LAB/LAB5/Task ', 'r', encoding='utf-8') as file:
    text_to_search = file.read()

# 解析内容
results = parse_receipt(text_to_search)
for item in results:
    print(f"商品: {item[0]}, 价格: {item[1]}")