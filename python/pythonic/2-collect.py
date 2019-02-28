引用
"What the fuck is this shit?" -- 这它吗的是什么鬼东西
"What the fuck?"
"一份优雅、干净、整洁的代码通常自带文档和注释属性，读代码即是读作者的思路。
Python 开发中很少要像 Java 一样把遵循某种设计模式作为开发原则来应用到系统中，
毕竟设计模式只是一种实现手段而已，代码清晰才是最终目的，而 Python 灵活而不失优雅，
这也是为什么 Python 能够深受 geek 喜爱的原因之一。"

如果是好的"What the fuck?" 衡量代码质量的唯一标准就是每分钟骂出"WTF" 的频率

1.链式比较操作
2.if/else 三目运算
    在类c的语言中都支持三目运算b?x:y. Python 之禅 有这么一句话:
        "There should be one -- and preferably only one-- obvious way to do it"
    能够用 if/else 清晰表达逻辑时, 就没有必要额外新增一种方式实现
3.真值判断
4.for/else
5.字符串格式化
    bad
        place = 'earth'
        address = 'I am from %s' % (place)
        print address # I am from earth

    good
        print 'I am from {place}'.format(place="earth")
        # I am from earth
    很难说使用 format 比用%s 的代码量少, 但是format 更易于理解
    "Explicit is better than implicit" -- Zend of Python
    -- 显性比隐性好

6.列表切片
    获取列表中的部分元素最先想到的就是用for 循环根据条件提取元素, 这也是其他语言中惯用的手段
    而在Python中还有强大的切片功能
    bad
        items = range(10)
        # 奇数
        add_items = []
        for i in items:
            if i % 2 != 0:
                add_item.append(i)

        # 拷贝
        copy_item = []
        for i in items:
            copy_items.append(i)

    good
        # 第1到第4个元素的范围区间
        sub_items = items[1:4]

        # 奇数
        odd_items = items[1::2]

        #copy

        copy_items = items[::] # or items[:]
    
    列表元素的下标不仅可以用正数表示，还可用负数表示，最后一个元素的位置是-1, 从右往左，依次递减

    p   y   t   h   o   n
    0   1   2   3   4   5
    -6  -5  -4  -3  -2  -1

7. 善用生成器
    
    def fib(n):
        a, b = 0, 1
        result = []
        while b , n:
            result.append(b)
            a, b = b, a+b
        return result
    
    pythonic
    def fib(n):
        a, b = 0, 1
        while a < n:
            yield a
            a, b = b, a + b

    评语: 用生成器申城斐波那契数列。生成器的好处就是无需一次性把所有元素加载到内容，只有迭代获取元素时才
    返回该元素，而列表是预先一次性把全部元素加载到了内存。此外用yield代码看起来更清晰。

8. 获取字典元素
    d = {"home":"SDLY"}
    if d.has_key("home"):
        print(d['home'])
    else:
        print("unknow")

    pythonic
    d.get("name", "unknow")

9. 预设字典默认值
    通过 key 分组的时候，不得不每次检查key是否存在于某个字典中

    
    data = [('foo', 20), ('bar', 30), ('foo', 40), ('ba', 50)]
    groups = {}
    for (key, value) in data:
        if key in groups:
            groups[key].append(value)
        else:
            groups[key] = [values]

    pythonic
    # 第一种方式

    groups = {}
    for (key, value) in data:
        groups.setefault[key, []].append(value)

    # 使用 collections 容器
    from collections import defaultdict
    groups = defaultdict(list)
    for (key, value) in data:
        groups[key].append(value)

10 字典推导式
    在python 2.7 之前, 构建字典对象一边使用下面这种方式，可读性非常差
    
    numbers = [1, 2, 3]
    m_dict = dict([(number, number *2) for number in numbers])
    print(my_dict) # {1: 2, 2: 4, 3: 6}

    pythonic

    numbers = [1, 2, 3]
    my_dict = {number: number * 2 for number in numbers}
    print(my_dict) {1: 2, 2: 4, 3: 6}
    # 还可以指定过滤条件
    my_dict = {number: number * 2 for number in numbers if number > 1}
    print(my_dict) # {2: 4, 3: 6}
    字典推导式式 python2.7 新增的特性, 可读性增强了很多，类似的还有
    列表推导式和集合推导式


