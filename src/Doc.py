from Paths import Paths
import calendar
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

def makeDoc(videoNum, isBatch):
    weekday = paths.today.weekday()
    date = paths.today.date
    doc = docTemplate.format(date, weekday, videoNum)
    # 写入每日统计结果md文件
    with open(paths.statis, 'w') as docFile:
        docFile.write(doc)

    # 更新README
    with open('../README.md', 'r') as README:
        monthName = calendar.month_name[paths.today.date.month]
        lines = README.readlines()
        yearLine = 0
        for i in range(len(lines)):
            line = lines[i]
            if 'h2' in line:
                yearLine = i + 1
                break

        # 新月份，写入新日历
        if paths.today.previousDay.month != paths.today.date.month and not isBatch:
            calen = makeCalendar(paths.today.date)
            calen = '<p align="center">\n\n' + calen + '</p>\n'
            lines.insert(yearLine, calen)
            monthNameUpdate = '\n<p align="center">\n\t' + monthName + '\n</p>\n\n'
            lines.insert(yearLine, monthNameUpdate)
            with open('../README.md', 'w') as README:
                README.writelines(lines)

        # 找到对应的月份更新
        dayLine = yearLine
        while not monthName in lines[dayLine]:
            dayLine += 1;
        dayLine += 5 # 定位到日历起点
        day = str(paths.today.date.day)
        day = ' ' + day + ' '
        for i in range(dayLine, dayLine + 7):
            line = lines[i]
            # 找到当前日期的单元格并修改为超链接
            if day in line:
                line = line.replace(
                    day,
                    '['+day[1:len(day) -1]+']'+'({})'.format(paths.statis[3:])
                )
                lines[i] = line
                break   # 不可删，否则8号可能会更新18号，28号的内容
                # TODO 解决上面break不可删的安全隐患
        with open('../README.md', 'w') as README:
            README.writelines(lines)

def makeCalendar(date):
    year = date.year
    month = date.month
    cal = calendar.monthcalendar(year, month)

    # 构建Markdown表格
    mdTable = "| Mon | Tue | Wed | Thu | Fri | Sat | Sun |\n"
    mdTable += "| --- | --- | --- | --- | --- | --- | --- |\n"

    for week in cal:
        mdTable += "| " + " | ".join(f"{day:2}" if day != 0 else "  " for day in week) + " |\n"
    mdTable += '\n'
    return mdTable

def batchProcess():
    now = str(paths.today.date)
    paths.changeDate('2023-08-25')
    while True:
        with open(paths.jsonPath, 'r') as f:
            data = json.load(f)
            videoNum = data['number']
            makeDoc(videoNum, True)
        nextDay = str(paths.today.nextDay)
        if nextDay == now:
            break
        else:
            paths.changeDate(nextDay)
    paths.changeDate(now)

if __name__ == "__main__":
    # testing code
    batchProcess()
