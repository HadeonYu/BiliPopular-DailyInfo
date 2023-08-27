from datetime import datetime

class Today:
    def __init__(self):
        self.date = datetime.date(datetime.now())  # 获取当前日期
        self.year = self.date.year  # 获取当前年份
        self.month = self.date.month  # 获取当前月份
        self.day = self.date.day  # 获取当前日期
        self.date = str(self.date)  # 将日期转换为字符串

    def selfDef(self, date):
        self.date = date  # 将日期属性设置为指定日期
        dateInfo = date.split('-')  # 将日期字符串按照'-'分割为列表
        for i in range(len(dateInfo)):
            dateInfo[i] = int(dateInfo[i])  # 将日期字符串转换为整数

class Paths:
    def __init__(self):
        self.today = Today()  # 创建Today对象，获取当前日期
        self.dailyPath = '../dailyData/' + str(self.today.date).replace('-','/')    # 每日数据文件夹路径
        self.jsonPath = self.dailyPath + '/list.json'   # JSON文件路径
        self.xlsxPath = self.dailyPath + '/detail.xlsx' # Excel文件路径
        self.mdPath = self.dailyPath + '/detail.md'     # Markdown文件路径

    def changeDate(self, date):
        self.today.selfDef(date)
        self.dailyPath = '../dailyData/' + str(self.today.date).replace('-','/')    # 每日数据文件夹路径
        self.jsonPath = self.dailyPath + '/list.json'   # JSON文件路径
        self.xlsxPath = self.dailyPath + '/detail.xlsx' # Excel文件路径
        self.mdPath = self.dailyPath + '/detail.md'     # Markdown文件路径

if __name__ == "__main__":
    exit()
