from Paths import Today, Paths
docTemplate = '''
<h2 align="center">{0} {1}</h2>

[详细数据](dailyData/{0}/detail.md)

**今日视频数量：579**

### 播放量统计
<p align="center">
    <img src="./dailyData/{0}/views.png" alt="播放量统计">
</p>

### 视频时长统计
#### 总体：
<p align="center">
    <img src="./dailyData/{0}/duration.png" alt="视频时长统计">
</p>

#### 短视频：
<p align="center">
    <img src="./dailyData/{0}/duraShort.png" alt="短视频时长统计">
</p>

### 子分区
<p align="center">
    <img src="./dailyData/{0}/section.png" alt="子分区统计">
</p>

### ip属地统计
<p align="center">
    <img src="./dailyData/{0}/ip.png" alt="ip属地统计">
</p>
'''

for i in range(25, 31, 1):
    date = '2023-08-' + str(i)
    today = Today()
    today.selfDef(date)
    weekday = today.weekday()
    doc = docTemplate.format(date, weekday)
    print(doc)
