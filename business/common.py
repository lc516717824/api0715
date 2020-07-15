'''
常用功能
'''
import requests
from business.request_sdk import do_request
# 发布话题
def create_topic(topic_data):
    url = "http://49.233.108.117:3000/api/v1/topics"
    return do_request(url=url,http='post', data=topic_data)
#话题详情
def get_topic_detail(topic_id):
    url = "http://49.233.108.117:3000/api/v1/topic/" + topic_id
    return do_request(url=url,http='get')
# 获取toke值
def get_token():
    return "1bc398ce-0ca6-4392-a125-9246a05454f8"