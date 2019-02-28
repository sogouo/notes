Pythonic -> Python + (很Python的写法).
简写说明:
P: Pythonic 的写法
NP: non-pythonic 的写法

-- 引用--
为什么要追求 Pythonic ?
"相比于NP, P 的写法简练、明确、优雅, 绝大部分的时候执行效率高, 代码越少也越不容易出错。
我认为好程序员在写代码时, 应该追求代码的正确性、简洁性和可读性，这恰恰就是Pythonic 的精神所在。"



1. 置换两个变量的值
   good:
       a, b = b, a
   
   bad:
       temp = a
       a = b
       b = temp

   原理: 通过元组的pack 和 unpack 完成了对a, b对互换，避免了使用临时变量temp, 而且只用了一行代码

2. 链式比较
    good:
        a = 3
        b = 1
        1 <=b <= a < 10 # True
    bad:
        b >= 1 and b <= a and a < 10 # True

3. 真值测试
    good
        name = 'Tim'
        langs = ['Java', 'Python', 'Go']
        info = {'name': 'Jone', 'language': 'engish'}

        if name and langs and info:
            print('Right') # Right

    bad
        if name != '' and leng(len(langs)) > 0 and info != {}:
            print('Right') # Right

    简言而止, P 的写法就是在对「任意对象」，直接判断其真假，无需写判断条件，这样既能保证正确性，又能减少代码量

    真假值表(记住了真假值你就能省很多代码）

    真                                          假

    True                                        False

    任意非空字符串                              空对字符串''

    任意非0数字                                 数字 0

    任意非空容器                                空的容器 {}, (), [], set()

    其他非任意False                             None


4. 字符串反转
    good
        def reverse_str(a):
            return s[::-1]

    bad
        def reverse_str(a):
            t = ''
            for x in xrange(len(s)-1, -1):
                t += s[x]
            return t

 5. 字符串列表的连接
    
    good
        strList = ['Life', 'short,', 'I', 'use', 'Python']
        res = ' '.join(strlist) # Life short, I use Python

    bad
        res = ''
        for s in strlist:
            res += s + ' '
        # 最后还多了余空格

6. 列表求和，最大值，最小值，乘积
    good
        numList = [1, 2, 3, 4, 5]
        sum = sum(numList)
        maxNum = max(numList) # maxNum = 5
        mixNum = min(numList) # minNum = 1
        from operator import mul
        prod = reduce(mul, numList, 1) # prod = 120, 默认值传1以防空列表

    bad
        sum = 0
        maxNum = -float('inf')
        minNum = float('inf')
        prod = 1
        for num in numList:
            if num > maxNum:
                maxNum = num
            if num < minNum:
                minNum = num
            sum += num
            prod *= num
        # sum = 15 maxNum = 5 minNum = 1 prod = 120

        经简单测试，在numList的长度为10000000时，在我的机器上对列表求和，
        P耗时0.6s，NP耗时1.3s，将近两倍的差距。所以不要自己造轮子了。


7. 列表推导式
    l = [x*x for x in range(10) if x % 3 == 0]
    #l = [0, 9, 36, 81]

    i = []
    for x in range(10):
        if x % 3 == 0:
            i.append(x*x)
8. 字典默认值
    good
        dic = {'course_name': '英语', 'course_time': '9:30 ~ 11:00'}
        dic['course_mark'] = dic.get('course_mark', 0) + 1
    bad
        if 'course_mark' in dic:
            dic['course_mark'] = 1
        else:
            dic['course_mark'] = 1

    dict 的get(key, default) 方法用于获取字典中key的值，若不存在
    key, 则将key默认值为default

9. for ... else .. 语句
    for x in xrange(1, 5):
        if x == 5:
            print 'find'
            break
    else:
        print 'can not find 5'

    bad
        find = False
        for x in xrange(1, 5):
            if x == 3:
                find = True
                print 'find'
                break
        if not find:
            print 'can not find'
    for ... else .. 的 else 部分用来处理没有从for 循环中断的情况。有了它，我们不用设置状态变量来检测for循环有break 
    出来，简单方便

10. 三元符的替代
    a = 3
    b = 2 if a > 2 else 1
    # b = 2

    bad
        if a > 2:
            b = 2
        else:
            b = 1
        #b = 2

11 Enumerate
    good
    array = [1, 2, 3, 4, 5]
    for i, ein enumerate(array, 0):
        print i, e

    bad
        for i in xrange(len(array)):
            print i, array[i]
    使用 enumerate 可以一次性将索引和值取出，避免使用索引来取值，而且enumerate 的第二个参数
    可以调整索引下标的起始位置，默认0

12. 使用zip 创建键值对
    good
        keys = ['skill', 'tool']
        values = ['None', 'vim']
        dic = dict(zip(keys, values))
        # {'skill': 'None', 'tool': 'vim'}
    
    bad
        dic = {}
        for i, e in enumerate(keys):
            dic[e]  = values[i]
        #


参考: http://wuzhiwei.net/be_pythonic/
    https://docs.python-guide.org/writing/style/
    https://pyzh.readthedocs.io/en/latest/python-idioms.html
    https://pyzh.readthedocs.io/en/latest/python-hidden-features.html
    https://jeffknupp.com/writing-idiomatic-python-ebook/

    大神博客: https://github.com/iWoz/DSinJS
    https://stackoverflow.com/users/1474999/tim

Python Enhancement Proposal -> Python 增强提案

