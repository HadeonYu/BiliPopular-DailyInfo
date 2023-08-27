import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import brewer2mpl
import json

from Paths import Paths

paths = Paths()
paths.changeDate('2023-08-25')

def detailExcel():  # 生成详细数据Excel文件
    with open(paths.jsonPath, 'r') as jsonFile:  # 打开每日数据文件
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
        df.to_excel(paths.xlsxPath, index = False)  # 将DataFrame对象写入Excel文件中
        df.to_markdown(paths.mdPath, index = True)  # 写入markdown
        return df

def viewsStatis(df):    #   统计播放量
    views = df['播放量']
    views = views / 1e6
    viewsMax = views.max()
    viewsMin = views.min()
    #   bins为区间边界， hist为区间的频数
    hist, bins = np.histogram(views, bins=10, range=(viewsMin, viewsMax))

    # 设置配色
    bmap = brewer2mpl.get_map('Set3', 'qualitative', 5)
    colors = bmap.mpl_colors
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置字体，不然中文无法显示

    # 画图
    plt.bar(bins[:-1], hist, width=(bins[1] - bins[0])- 0.05,
            align='edge', color=colors)
    # 在每个柱子顶部显示纵坐标值
    for i, v in enumerate(hist):
        plt.text(bins[:-1][i] + 0.25, v + 1, str(v), ha='center', va='bottom')
    plt.xlabel('播放量/百万次')
    plt.ylabel('视频数量')
    plt.title('播放量分布情况')
    plt.savefig(paths.viewPic)
    plt.close()
    #plt.show()

def ipStatis(df):
    ip = df['ip属地']
    ipCounts = ip.value_counts()
    ipCounts = ipCounts.sort_values(ascending=True)

    # 设置配色
    bmap = brewer2mpl.get_map('Set3', 'qualitative', 5)
    colors = bmap.mpl_colors
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置字体，不然中文无法显示

    #画图
    plt.rcParams['figure.figsize']=(7.2, 12.8)
    plt.barh(ipCounts.index, ipCounts.values, color = colors)
    plt.xlabel('数量')
    plt.ylabel('ip属地')
    plt.yticks(rotation=30)
    plt.title('ip属地分布情况')
    plt.tight_layout()
    plt.savefig(paths.ipPic)
    #plt.show()
    plt.close()


def sectionStatis(df):
    sec = df['子分区']

if __name__ == "__main__":
    df = detailExcel()
    viewsStatis(df)
    ipStatis(df)
