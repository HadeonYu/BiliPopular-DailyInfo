import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import brewer2mpl
from PIL import Image
from wordcloud import WordCloud
import json

from Paths import Paths

paths = Paths()
#paths.changeDate('2023-08-27')

def detail():  # 生成详细数据Excel文件
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
    views = views / 1e5
    bins = np.arange(0, 30.1, 2.5)
    if views.max() > 30:
        bins = np.append(bins, views.max())
    #   bins为区间边界， hist为区间的频数
    hist, _ = np.histogram(views, bins=bins)

    # 设置配色
    bmap = brewer2mpl.get_map('Set3', 'qualitative', 5)
    colors = bmap.mpl_colors
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置字体，不然中文无法显示

    # 画图
    plt.bar(bins[:-1], hist, width=(bins[1] - bins[0]),
            align='edge', color=colors)
    # 在每个柱子顶部显示纵坐标值
    for i, v in enumerate(hist):
        plt.text(bins[:-1][i] + 0.9, v + 1, str(v), ha='center', va='bottom')

    plt.xlabel('播放量/十万次')
    plt.ylabel('视频数量')
    plt.title('播放量分布情况')
    plt.savefig(paths.viewPic, dpi=300)
    #plt.show()
    plt.close()

def ipStatis(df):
    ip = df['ip属地']
    ipCounts = ip.value_counts()
    ipCounts = ipCounts.sort_values(ascending=True)

    # 设置配色
    bmap = brewer2mpl.get_map('Set3', 'qualitative', 5)
    colors = bmap.mpl_colors
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置字体，不然中文无法显示

    #画图
    plt.rcParams['figure.figsize']=(7.2, 8.2)
    plt.barh(ipCounts.index, ipCounts.values, color = colors)

    # 柱子右侧显示数值
    for i, value in enumerate(ipCounts.values):
        plt.text(value + 1, i, str(value), ha='left', va='center')

    plt.xlabel('数量')
    plt.ylabel('ip属地')
    #plt.yticks(rotation=30)
    plt.title('ip属地分布情况')
    plt.tight_layout()
    plt.savefig(paths.ipPic, dpi=300)
    #plt.show()
    plt.close()

def durationStatis(df):
    dura = df['平均每P时长/秒']
    dura = dura / 60    # 秒转为分钟
    bins = np.arange(0, 30.1, 2.5)
    if dura.max() > 30:
        bins = np.append(bins, dura.max())
    hist, _ = np.histogram(dura, bins=bins)

    # 设置配色
    bmap = brewer2mpl.get_map('Set3', 'qualitative', 5)
    colors = bmap.mpl_colors
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置字体，不然中文无法显示

    # 画图
    plt.bar(bins[:-1], hist, width=(bins[1] - bins[0]),
            align='edge', color=colors)
    # 在每个柱子顶部显示纵坐标值
    for i, v in enumerate(hist):
        plt.text(bins[:-1][i] + 0.9, v + 1, str(v), ha='center', va='bottom')

    plt.xlabel('视频时长/分钟')
    plt.ylabel('视频数量')
    plt.title('视频时长总体分布情况')
    plt.savefig(paths.duraPic, dpi=300)
    #plt.show()
    plt.close()

    # 短视频分布情况
    bins = np.arange(0, 5.1, 0.5)
    hist, _ = np.histogram(dura, bins=bins)
    plt.bar(bins[:-1], hist, width=(bins[1] - bins[0]),
            align='edge', color=colors)
    # 在每个柱子顶部显示纵坐标值
    for i, v in enumerate(hist):
        plt.text(bins[:-1][i] + 0.3, v + 1, str(v), ha='center', va='bottom')

    plt.xlabel('视频时长/分钟')
    plt.ylabel('视频数量')
    plt.title('短视频分布情况')
    plt.savefig(paths.duraShortPic, dpi=300)
    #plt.show()
    plt.close()

def sectionStatis(df):
    sec = df['子分区']
    text = ' '.join(sec)

    # 词云背景图
    #bgImg = Image.open(paths.biliLogo)
    #bgImg = np.array(bgImg)
    # 生成词云
    wc = WordCloud(
        background_color='white',
        max_words=100,
        width=1920,
        height=1440,
        #mask=bgImg,
        font_path=paths.font
    )
    wc.generate(text)
    # 写入文件
    wc.to_file(paths.sectionPic)

def process():
    df = detail()
    viewsStatis(df)
    ipStatis(df)
    durationStatis(df)
    sectionStatis(df)

if __name__ == "__main__":
    #paths.changeDate('2023-09-08')
    print(paths.today.date)
    process()
