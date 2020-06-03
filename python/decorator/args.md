1. Python 装饰器是如何获取被装饰函数的参数的

```python
def debug(func):
    def wrapper(*args, **kwargs):
        print "[DEBUG]: enter {}()".format(func.__name__)
        print 'Prepare and say...',
        return func(*args, **kwargs)
    return wrapper

@debug
def say(something):
    print "hello {}!".format(something)

```

```python
# debug 返回的是函数wrapper 所以
@debug
def say(something):
    print "hello {}!".format(something)
# 等价于
debug(say)(something)
# 等价于
wrapper(something)
# 从 def wrapper(*args, **kwargs)可知，something传递到了*args中
```

https://segmentfault.com/q/1010000013177189


python 装饰器返回值问题

https://segmentfault.com/q/1010000000345122

https://docs.spring.io/spring/docs/2.0.8/reference/aop.html

https://blog.csdn.net/JackLiu16/article/details/81152956
