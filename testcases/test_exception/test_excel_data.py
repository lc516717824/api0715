import pytest
import json
import business.file_utils as fl
from business.request_sdk import do_request
from business.common import *
import requests

test_data = fl.parse_from_excel('data/data.xlsx','topics')
# pytest
@pytest.mark.parametrize('url,http,topic_data,code,msg',test_data)
def test_create_topic(url,http,topic_data,code,msg):
     # 发布话题
    if http == 'post':
        # print(topic_data)
        res = do_request(url=url,http=http,data=json.loads(topic_data))
        # res = requests.post(url=url,data=topic_data)
        # 发送请求 获得json 数据
        jsondata = res.json()
        # 断言
        assert res.status_code == code
        assert jsondata['success'] == json.loads(msg)['success']
        assert jsondata['error_msg'] == json.loads(msg)['error_msg']

def test_reply_topic():
    # 新建评论
    dict_data = {
        "accesstoken":get_token(),
        "title":"超级大魔王",
        "tab":"ask",
        "content":"等待修改"
    }
    # print(create_topic(dict_data).json())
    # 发布一个 话题 获取topic_id
    topic_id = create_topic(dict_data).json()['topic_id']
    url = "http://49.233.108.117:3000/api/v1"+ f"/topic/{topic_id}/replies"
    reply_data = {
        "accesstoken":get_token(),
        "content":"修改完毕"
    }
    # 对发布的话题 进行评论 post
    res = do_request(url = url, http='post',data= reply_data)
    # 断言
    assert res.status_code == 200
    # 话题详情 断言
    replt_res = get_topic_detail(topic_id)
    assert reply_data['content'] in replt_res.json()['data']['replies'][0]['content']

