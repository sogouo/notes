

问题一: 将序列中的元素以指定字符分割生成一个新字符串

内置函数 join() 与之对应的是split()
语法格式
   str.join(sequence)
   str: 指定分割的字符
   sequence: 要连接的元素序列

备注: 与php 对应的是 implode() -> explode()

```python
   fruits = ('orange', 'pear', 'apple', 'banana')
   print(", ".join(fruits))
  
   fruits = {'orange', 'pear', 'apple', 'banana'}
   print(", ".join(fruits))

   fruits = ['orange', 'pear', 'apple', 'banana']
   print(", ".join(fruits))
   
```
结果
<img src="./images/join.png"  alt="图片名称" align=center />
```php
   <?php
   fruits = array('orange', 'pear', 'apple', 'banana');
   var_dump(implode(', ', fruits));


```
结果
<img src="./images/php-implode.png" alt="图片名称" align=center />


问题二: 将字符串中的old(旧字符串)替换成new(新字符串)

replace 语法
    str.replace(old, new[, max])

    参数
    old: 将被替换的子字符串
    new: 新字符串, 用于替换old子字符串
    max: 可选字符串, 替换不超过max 次

    返回值 返回字符串中的old(旧字符串)替换成new（新字符串)后生成的新字符串，

    tag = "I love Python"
    print tag.replace("love", "like") # 替换之后生成新的字符串
    print tag # 原来tag
特殊声明: replace 不会改变原来 string 的内容

https://www.cnblogs.com/yes123/p/5279843.html


感谢:
    廖雪峰老师的blog
    RUNoob 菜鸟教程
    网易北京理工大学教程



list 循环

enumerate(sequence, [start=0])
sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置。



python getattr
https://docs.python.org/2/library/functions.html
https://www.cnblogs.com/cenyu/p/5713686.html
https://www.runoob.com/python/python-func-getattr.html
https://segmentfault.com/q/1010000000713465



pip 升级以及设置
https://www.runoob.com/w3cnote/python-pip-install-usage.html


#### Python Dictionary update function
>  将字典dict2 的键/值对更新到dict 里
>  1. update() 方法语法:
>     > dict.update(dict2)
>  2. 参数
>     > dict2 -- 添加到指定字典dict里到字典
>  3. 返回值
>     > 该方法没有任何返回值
>
>  4. 如果有相同的键会直接替换成update的值
