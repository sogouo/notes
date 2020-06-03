1W602: deprecated form of raising exception

Best example:
```python
if condition == True:
    raise ValueError(HELPING_EXPLANATION)
```
Bad
```python
if condition == True:
    raise ValueError, 'message'
```

https://code-examples.net/en/q/b6fa55



遇到问题:
W602: deprecated form of raising exception
C901 '' is too complex (13) [mccabe]




https://www.python.org/dev/peps/pep-0008/#imports

Flask*8Rules

https://lintlyci.github.io/Flake8Rules/



### Python 编码规范

#### 一、PyLint

##### 一、message 常注意到问题

##### 1）、`pylint no-else-raise`

```python
# bad way
a = "a"
b = "b"
c = "c"
if a != b
    raise 
elif a != c:
		raise

# Best way
if a != b:
    raise
if a != c:
    raise

# The raise causes control flow to be disrupted - so you don't need to use elif and can use if instead
# The else part of elif is redundant in this case, because the raise will exit the block
```

[pylint R1720: Unnecessary “elif” after “raise” (no-else-raise)](https://stackoverflow.com/questions/55632832/pylint-r1720-unnecessary-elif-after-raise-no-else-raise)

[中文翻译](https://stackoom.com/question/3lQdk/pylint-R-%E5%8A%A0%E6%B3%A8-%E5%90%8E%E4%B8%8D%E5%BF%85%E8%A6%81%E7%9A%84-elif-no-else-raise)

[R1705 (no-else-return): Also apply for "raise"](https://github.com/PyCQA/pylint/issues/2558)

##### 2）`pylint no-self-use] Method could be a function`

[Method could be a function](https://docs.quantifiedcode.com/python-anti-patterns/correctness/method_could_be_a_function.html)

[How to handle the pylint message: Warning: Method could be a function](https://stackoverflow.com/questions/2674035/how-to-handle-the-pylint-message-warning-method-could-be-a-function)

```python
@classmethod
def spam(cls, ...):
  
@staticmethod
def spam(cls)
```

**R0201**： Method could be a function

###### Description：Used when there is no reference to the class, suggesting that the method could be used as a static function instead

###### Explanation：If the class method does not reference any of the class attributes it may be more clear to define the method as a static function instead.

Attempt using either of the decorators @classmethod or @staticmethod



Example：

```python
Class Foo(object):
    ...
    def bar(self, baz):
        ...
        return llama
```



Try instead to use:

```python
Class Foo(object):
    ...
    @classmethod
    def bar(cls, baz):
        ...
        return llama
```

[**R0201**](http://pylint-messages.wikidot.com/messages:r0201)

[Understanding and Solving pylint errors for Python 3](https://www.gyanblog.com/gyan/python-pylint-errors-solution/)





### 问题

#### 1、SQLAlchemy 日常使用问题

1）、查询用户列表中不包含那些用户，解决方案 `WHERE id not in ()`

```python
# sql: SELECT * FROM `user` WHERE id not in (1, 2);

# init db: sessoin and User Model


users = User.query.filter_by(~id.in([1,2])).all()

# 相反
users = User.query.filter_by(id.in([1,2])).all()
```

[How to use NOT IN clause in sqlalchemy ORM query](https://stackoverflow.com/questions/26182027/how-to-use-not-in-clause-in-sqlalchemy-orm-query)

key: flask sqlalchemy not in

