# -*- coding: utf-8 -*-

def sumOfN(n):
    """
        该算法初始化值为 0 的累加器(accumulator) 变量
        然后迭代n个整数, 将每个依次添加到累加器。
    """
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum +i

    return theSum

print(sumOfN(10))

def foo(tom):
    """
        乍一看，它很奇怪，但进一步观察，你可以看到这个函数本质上和
        前一个函数做同样到事情。不直观到原因在于编码习惯不好。我们没有
        使用良好到标识符(identifier)名称来提升可读性，我们在迭代步骤中使用了
        一个额外到赋值语句，这并不是真正必要的
    """
    fred = 0
    for bill in range(1, tom+1):
        barney = bill
        fred = fred + barney
    return fred

print(foo(10))



