import pandas as pd
import json
from Paths import Paths

def detailExcel():  # 生成详细数据Excel文件
    paths = Paths()
    with open(paths.jsonPath(), 'r') as jsonFile:  # 打开每日数据文件
        jsonData = json.load(jsonFile)  # 读取JSON格式数据
        detailData = []  # 定义空列表，用于存储视频详细信息
        for video in jsonData['list']:
            if not 'pub_location' in video:
                ip = {'pub_location':'未知'}
                video.update(ip)
            singleVideoDetail = {
                '标题':video['title'],
                '平均每P时长/秒':video['duration'] / video['videos'],
                '子分区':video['tname'],
                '播放量':video['stat']['view'],
                '点赞':video['stat']['like'],
                '硬币':video['stat']['coin'],
                '收藏':video['stat']['favorite'],
                '分享':video['stat']['share'],
                '评论数':video['stat']['reply'],
                '弹幕量':video['stat']['reply'],
                'up主':video['owner']['name'],
                '粉丝量':video['owner']['follower'],
                'ip属地':video['pub_location']
            }
            detailData.append(singleVideoDetail)  # 将单个视频详细信息添加到列表中
        df = pd.DataFrame()  # 创建空的DataFrame对象
        for info in detailData:  # 遍历视频详细信息列表
            df = df._append(info, ignore_index = True)  # 将单个视频详细信息添加到DataFrame对象中
        df.to_excel(paths.xlsxPath(), index = False)  # 将DataFrame对象写入Excel文件中
        df.to_markdown(paths.mdPath(), index = True)

if __name__ == "__main__":
    detailExcel()
