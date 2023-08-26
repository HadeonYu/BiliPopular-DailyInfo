from datetime import datetime

class Today:
    def __init__(self):
        self.date = datetime.date(datetime.now())  # 获取当前日期
        self.year = self.date.year  # 获取当前年份
        self.month = self.date.month  # 获取当前月份
        self.day = self.date.day  # 获取当前日期
        self.date = str(datetime.date(datetime.now()))  # 将日期转换为字符串

    def selfDef(self, date):
        self.date = date  # 将日期属性设置为指定日期
        dateInfo = date.split('-')  # 将日期字符串按照'-'分割为列表
        for i in range(len(dateInfo)):
            dateInfo[i] = int(dateInfo[i])  # 将日期字符串转换为整数

class Paths:
    def __init__(self):
        self.today = Today()  # 创建Today对象，获取当前日期
        #self.today.selfDef('2023-08-25')

    def dailyPath(self):
        dailyPath = str(self.today.date).replace('-','/')  # 将日期字符串中的'-'替换为'/'
        return '../dailyData/' + dailyPath  # 返回每日数据存储路径

    def jsonPath(self):
        return self.dailyPath() + '/list.json'  # 返回每日数据JSON文件路径

    def xlsxPath(self):
        return self.dailyPath() + '/detail.xlsx'  # 返回每日数据Excel文件路径

    def mdPath(self):   # 返回每日数据Markdown文件路径
        return self.dailyPath() + '/detail.md'
