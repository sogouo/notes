
1. 月和星期变量命名
```Python
# Weekday and month names for HTTP date/time formatting; always English!

____WEEKDAYNAME = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
_MONTHNAME = [None,  # Dummy so we can use 1-based month numbers
              "Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

```


声明一个函数
```python
def format_date_time(timestamp):
    # Return a byte-string of the date and time in HTTP format
    # .. versionchanged:: 1.1b5
    #  Return a byte string, not a native string
    year, month, day, hh, mm, ss, wd, _y, _z = time.gmtime(timestamp)
    value = "%s, %02d %3s %4d %02d:%02d:%02d GMT" % (_WEEKDAYNAME[wd], day, _MONTHNAME[month], year, hh, mm, ss)
    if PY3:
        value = value.encode("latin-1")
    return value
```

调用
```python
format_date_time(time.time())
```

_全部大写, 在python中表示什么变量


must not be blank 不能为空

```python

def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')
```

