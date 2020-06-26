

```mysql
-- mysql 日常更新, 慎用 replace
-- replace(field_name, from_str, to_str)
-- field_name: 字段名
-- from_str: 需要替换的字符串
-- to_str: 替换成的字符串
-- 该函数是多字节安全的,也就是说你不用考虑是中文字符还是英文字符.
-- UPDATE `table_name` SET field_name = replace(field_name, from_str, to_str) WHERE 
```


