import pytest
import json
import business.file_utils as fl
from business.request_sdk import do_request
import requests

test_data = fl.parse_from_excel('data/data.xlsx','topics')
# pytest
@pytest.mark.parametrize('url,http,topic_data,code,msg',test_data)
def test_create_topic(url,http,topic_data,code,msg):
     # 发布话题
    if http == 'post':
        print(topic_data)
        res = do_request(url=url,http=http,data=json.loads(topic_data))
        # res = requests.post(url=url,data=topic_data)
        # 发送请求 获得json 数据
        jsondata = res.json()
        # 断言
        assert res.status_code == code
        assert jsondata['success'] == json.loads(msg)['success']
        assert jsondata['error_msg'] == json.loads(msg)['error_msg']