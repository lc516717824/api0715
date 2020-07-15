"""
主要测试 cond社区的话题相关的功能
主要API包括
1。 主题首页
"""
import requests
import business.common as common

def test_topic_page():
    # 主题首页功能 get
    url = 'http://49.233.108.117:3000/api/v1/topics'
    getdata = {"page": 1, "tab": "ask", "limit": 5, "mdrender": "true"}
    r = requests.get(url=url, params=getdata)
    json_data = r.json()['data']
    assert len(json_data) == getdata['limit']
    for i in json_data:
        assert i['tab'] == 'ask'


def test_create_topic():
    # 创建主题
    create_url = "http://49.233.108.117:3000/api/v1/topics"
    post_data = {"accesstoken": common.get_token(),
                 "title": "新世111界",
                 "tab": "ask",
                 "content": "你好~欢迎来到新世界~！"}
    r1 = requests.post(url=create_url, data=post_data)
    r2 = requests.post(url=create_url, data=post_data)
    assert r1.status_code == 200
    r1_topic_id = r1.json()['topic_id']
    r2_topic_id = r2.json()['topic_id']
    assert r1_topic_id != r2_topic_id


def test_topic_detail():
    post_data = {"accesstoken": common.get_token(),
                 "title": "你要发财了",
                 "tab": "ask",
                 "content": "你好~欢迎来到新世界~"}
    # 返回 topic_id 的值
    topic_id = common.create_topic(post_data).json()['topic_id']
    # 主题详情 get
    # url = "http://49.233.108.117:3000/api/v1/topic/"+topic_id
    res = common.get_topic_detail(topic_id)
    assert res.status_code == 200
    jsondata = res.json()
    # 断言字段详情页 与 发送页 输入内容是否相符合
    assert post_data['title'] == jsondata['data']['title']
    assert post_data['tab'] == jsondata['data']['tab']
    assert post_data['content'] in jsondata['data']['content']


def test_topic_update():
    # 编辑主题
    post_data = {"accesstoken": common.get_token(),
                 "title": "你要发财了",
                 "tab": "ask",
                 "content": "你好~欢迎来到新世界~"}
    # 返回 topic_id 的值
    topic_id = common.create_topic(post_data).json()['topic_id']
    # 编辑话题
    url = 'http://49.233.108.117:3000/api/v1/topics/update'
    update_data = {"accesstoken": common.get_token(),
                 "title":"世界末日了",
                 "topic_id": topic_id,
                 "tab": "ask",
                 "content": "你好~欢迎来到世界末日~"}
    res = requests.post(url =url,data = update_data)
    #更新后的id与原来更新之前的id保持一致
    update_topic_id = res.json()['topic_id']
    assert topic_id == update_topic_id
    #更新之后新内容的断言
    #1.获取更新后之后的内容
    res = common.get_topic_detail(update_topic_id)
    jsondata = res.json()
    #2.断言
    assert update_data['title'] == jsondata['data']['title']
    assert update_data['tab'] == jsondata['data']['tab']
    assert update_data['content'] in jsondata['data']['content']