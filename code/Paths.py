from datetime import datetime

class Today:
    def __init__(self):
        self.date = datetime.date(datetime.now())  # 获取当前日期 

    def selfDef(self, date):
        self.date = datetime.strptime(date, '%Y-%m-%d')

    def weekday(self):  # 返回星期
        weekdayNumber = self.date.weekday()
        weekdayList = ['一', '二', '三', '四', '五', '六', '日']  # 获取星期做准备
        return '星期' + weekdayList[weekdayNumber]

class Paths:
    def __init__(self):
        self.today = Today()  # 创建Today对象，获取当前日期
        self.specificPath()

    def changeDate(self, date):
        self.today.selfDef(date)
        self.specificPath()

    def specificPath(self):
        self.font = '../src/simsun.ttf' #字体文件，用于生产词云
        self.biliLogo = '../src/biliLogo.jpeg'
        self.dailyPath = '../dailyData/' + str(self.today.date).replace('-','/')    # 每日数据文件夹路径
        self.jsonPath = self.dailyPath + '/list.json'   # JSON文件路径
        self.xlsxPath = self.dailyPath + '/detail.xlsx' # Excel文件路径
        self.mdPath = self.dailyPath + '/detail.md'     # Markdown文件路径
        self.viewPic = self.dailyPath + '/views.png'    # 播放量统计图
        self.sectionPic = self.dailyPath + '/section.png'# 视频分区
        self.duraPic = self.dailyPath + '/duration.png' # 视频时长
        self.duraShortPic = self.dailyPath + '/duraShort.png'   # 短视频
        self.fansPic = self.dailyPath + '/fans.png'     # 粉丝数量
        self.ipPic = self.dailyPath + '/ip.png'         # ip属地
        self.statis = self.dailyPath + '/statistic.md'  # 统计结果文档




if __name__ == "__main__":
    exit()
