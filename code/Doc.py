from Paths import Paths
import json
docTemplate = '''<h2 align="center">{0} {1}</h2>

[详细数据](detail.md)

**今日视频数量：{2}**

### 播放量统计
<p align="center">
    <img src="views.png" alt="播放量统计">
</p>

### 视频时长统计
#### 总体：
<p align="center">
    <img src="duration.png" alt="视频时长统计">
</p>

#### 短视频：
<p align="center">
    <img src="duraShort.png" alt="短视频时长统计">
</p>

### 子分区
<p align="center">
    <img src="section.png" alt="子分区统计">
</p>

### ip属地统计
<p align="center">
    <img src="ip.png" alt="ip属地统计">
</p>'''
paths = Paths()

def makeDoc(videoNum):
    weekday = paths.today.weekday()
    date = paths.today.date
    doc = docTemplate.format(date, weekday, videoNum)
    # 写入每日统计结果md文件
    with open(paths.statis, 'w') as docFile:
        docFile.write(doc)

    # 更新README
    with open('../README.md', 'r') as README:
        lines = README.readlines()
        updateLine = 0
        for i in range(len(lines)):
            line = lines[i]
            if line == '## 正文：\n':
                updateLine = i + 1
                break
        text = str(paths.today.date)[5:]
        text = '\n<font size="4">[' + text + ']' + '({})</font>'.format(paths.statis[3:]) + '\n'
        lines.insert(updateLine, text)
        with open('../README.md', 'w') as README:
            README.writelines(lines)

if __name__ == "__main__":
    paths.changeDate('2023-08-25')
    now = '2023-09-03'
    while True:
        with open(paths.jsonPath, 'r') as f:
            data = json.load(f)
            videoNum = data['number']
            makeDoc(videoNum)
        nextDay = paths.today.nextDay
        if nextDay == now:
            break
        else:
            paths.changeDate(nextDay)
