'''
常用功能
'''
import requests
# 发布话题
def create_topic(topic_data):
    create_url = "http://49.233.108.117:3000/api/v1/topics"
    res_create_topic = requests.post(url = create_url, data = topic_data)
    topic_id = res_create_topic.json()['topic_id']
    return topic_id
#话题详情
def get_topic_detail(topic_id):
    url = "http://49.233.108.117:3000/api/v1/topic/" + topic_id
    res = requests.get(url)
    return res
# 获取toke值
def get_token():
    return "1bc398ce-0ca6-4392-a125-9246a05454f8"