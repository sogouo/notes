
问题一: 比较两个(日期)时间的大小

    1.如果是日期字符串例如"2019-06-26" "2019-06-27"
        思路: 将字符转换为datetime对象，然后在做减法

        datetime.strptime("2019-06-26", "%Y-%m-%d")

        datetime.strptime("字符串日期", "日期格式化模式")
        
        def compared_str_date(start_date, end_date):
            """
            :param start_date 开始日期字符串
            :param end_date 结束日期字符串
            """
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d)
            return (end_date - start_date).days > 0


问题二: 将datimetime 对象转换为格式化字符串
    datetime_obj.strftime("%Y-%m-%d)


问题三:输出指定格式的日期
    输出今日日期，格式化dd/mmyyy, 跟多选项可以查看 strftime()方法
    print datetime.date.today().strftime('%d/%m%Y')

    # 创建日期对象
    date_obj = datetime.date(2019, 6, 1)
    print date_obj.strftime('%d/%m%Y')

    # 日期算法运算
    add_one_day_obj = date_obj + datetime.timedelta(days=1)
    print date_obj.strftime('%d/%m%Y')

    # 日期替换
    print date_obj.replace(year=date_obj.year + 1)




学习
https://www.runoob.com/python/python-exercise-example16.html

