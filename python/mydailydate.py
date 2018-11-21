# -*- coding: utf-8 -*-

"""关于命名不规范灰常👏走过路过大神瞬时指出
    官方文档: https://docs.python.org/2/library/datetime.html

    日常项目或者练习关于 datetime 模块的总结与Demo
"""

from datetime import timedelta, datetime, date

class MyDailyDate():
    def get_day_of_each_month_in_datetime(self, *args):
        """ 通过 datetime 对象获取上个月1号零时或者任何x号datetime 对象
        """
        return (datetime.utcnow().replace(day=1, hour=0, second=0, minute = 0,  microsecond=0) - timedelta(days=1)).replace(day=1)

    def get_day_of_each_month_in_date(self, *args):
        """ as same as: get_day_of_each_month_in_datetime
        """
        return (date.today().replace(day=1) - timedelta(days=1)).replace(day=1)

    
mydaily = MyDailyDate()
datetime_day = mydaily.get_day_of_each_month_in_datetime()
date_day = mydaily.get_day_of_each_month_in_date()
print("{0} 的类型是 {1}".format(datetime_day, type(datetime_day)))
print("{0} 的类型是 {1}".format(date_day, type(date_day)))


""" 有时候, 通过 Model 类型按照日期字符串查询，且数据库中存储时间或者日期类型是datetime 类型,
    客户端传入是格式化日期字符串: eg. '2018-11-21'
    需要将日期函数转换为datetime类型: datetime.strftime(date_string, format)
"""

print("{0} 被格式化日期字符串 {1}".format(datetime_day, datetime.strftime(datetime_day,  "%Y-%m-%d")))




"""
    References 
    python date of the previous month
    https://stackoverflow.com/questions/9724906/python-date-of-the-previous-month

    




"""
