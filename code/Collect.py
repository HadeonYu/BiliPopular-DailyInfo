import requests
import json
import os
from datetime import datetime

from requests.api import request

url = 'https://api.bilibili.com/x/web-interface/popular'  # 定义API接口URL

def getData():  # 定义获取数据的函数
    params = {
        'pn':1,  # 访问的页码
    }
    videosInfo = []  # 定义空列表，用于存储视频信息
    while True:  # 循环获取数据
        resp = requests.get(url, params)  # 发送GET请求，获取数据
        if resp.status_code == 200:  # 判断请求是否成功
            respJson = resp.json()  # 将响应内容转换为JSON格式
            videosInfo.extend(respJson['data']['list'])  # 将视频信息添加到列表中
            if not respJson['data']['no_more']:  # 判断是否还有更多数据
                params['pn'] += 1  # 更新页码，获取下一页数据
            else:
                break  # 如果没有更多数据，退出循环
        else:
            print(resp.status_code)  # 如果请求失败，打印HTTP状态码
            break

    data = {
        'number':len(videosInfo),  # 记录视频数量
        'list':videosInfo  # 记录视频信息列表
    }
    for i in range(len(videosInfo)):    # 获取up主粉丝数
        mid = videosInfo[i]['owner']['mid'] # up主的mid
        statResp = requests.get('https://api.bilibili.com/x/relation/stat?vmid=' + str(mid))
        if statResp.status_code == 200:
            statJson = statResp.json()
            follower = {'follower':statJson['data']['follower']}
            videosInfo[i]['owner'].update(follower) # 粉丝数信息加入到owner值中
        else:
            print(resp.status_code)
    date = str(datetime.now().date())  # 获取当前日期
    dailyPath = '../dailyData/' + date  # 定义每日数据存储路径
    if not os.path.exists(dailyPath):  # 判断路径是否存在
        os.mkdir(dailyPath)  # 如果不存在，创建路径
    with open(dailyPath + '/list.json', 'w') as daily:  # 打开每日数据文件
        json.dump(data, daily, ensure_ascii = False, indent = 2)  # 将数据写入文件，格式化输出
if __name__ == "__main__":
    getData()
