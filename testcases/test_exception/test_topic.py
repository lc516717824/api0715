'''
测试异常场景
'''
import requests
import pytest
import business.file_utils as fl

# 发布话题
# data = json.load(open('data/topics.json',mode='r',encoding='utf8'))
# test_data = data['test_data']
test_data = fl.parse_from_json ('data/topics.json','test_data')
# 自动化生成测试用例
# 数据模型 topic_data数据 code data返回的状态码 error_msg返回的报错信息
@pytest.mark.parametrize('topic_data,code,errormsg', test_data)
def test_create_topic(topic_data,code,errormsg):
    url = "http://49.233.108.117:3000/api/v1/topics"
    # print(topic_data)
    res = requests.post(url, data=topic_data)
    jsondata = res.json()
    assert jsondata['success'] == False
    assert res.status_code == code
    assert jsondata['error_msg'] == errormsg
    # print(res.status_code,jsondata) # 打印的内容
