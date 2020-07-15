import json

#  编码
test = ['foll', {'lc': ('cong', 1, None, [5, 65, 7])}]
test_data = json.dumps(test)
print(test_data, type(test_data))
#  解码
test_str = '{"username":"liucong"}'
test_str_data = json.loads(test_str)
print(test_str_data, type(test_str_data))
#  解析文件
data = json.load(open('data/topics.json', mode='r', encoding='utf8'))
print(data, type(data))
#  写入文件
tmp = json.dump(test, open('data/tmp.json', mode='w', encoding='utf8'))
