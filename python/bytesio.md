

[Python 文件读写、StringIO和BytesIO](https://www.jianshu.com/p/b74a83e0f9fc)

[Python3-StringIO和BytesIO的总结](https://blog.csdn.net/yang_bingo/article/details/84066217)

[h[ow do i convert from '_io.BytesIO' to a bytes-like object in python3.6?](https://stackoverflow.com/questions/54137790/how-do-i-convert-from-io-bytesio-to-a-bytes-like-object-in-python3-6)](https://stackoverflow.com/questions/54137790/how-do-i-convert-from-io-bytesio-to-a-bytes-like-object-in-python3-6)



[python3 _io.BytesIO object write to redis]()

```python
# 将图片写入到excel表中
# xlsxwriter package
# py3venv/lib/python3.7/site-packages/xlsxwriter/worksheet.py
@convert_cell_args
def insert_image(self, row, col, filename, options=None):
    """
    Insert an image with its top-left corner in a worksheet cell.
		
		在工作表单元格中插入从左上角的图片
    Args:
        row:      The cell row (zero indexed).
        col:      The cell column (zero indexed).
        filename: Path and filename for image in PNG, JPG or BMP format.
        options:  Position, scale, url and data stream of the image.

    Returns:
        0:  Success.
        -1: Row or column is out of worksheet bounds.

    """
    # Check insert (row, col) without storing.
    if self._check_dimensions(row, col, True, True):
        warn('Cannot insert image at (%d, %d).' % (row, col))
        return -1

    if options is None:
        options = {}

    x_offset = options.get('x_offset', 0)
    y_offset = options.get('y_offset', 0)
    x_scale = options.get('x_scale', 1)
    y_scale = options.get('y_scale', 1)
    url = options.get('url', None)
    tip = options.get('tip', None)
    anchor = options.get('object_position', 2)
    image_data = options.get('image_data', None)

    # For backward compatibility with older parameter name.
    anchor = options.get('positioning', anchor)

    if not image_data and not os.path.exists(filename):
        warn("Image file '%s' not found." % force_unicode(filename))
        return -1

    self.images.append([row, col, filename, x_offset, y_offset,
                        x_scale, y_scale, url, tip, anchor, image_data])


 
# python3 BytesIO
import urllib.request
from io import BytesIO


def write_file_stream_to_redis(url):
    """Download file stream to redis
    """
    # redis 资源
    redis_source = ""
    file_stream = redis_source.get(key)
    if not file_stream:
        # 将字节流写入到缓存
        stream = BytesIO(
            urllib.request.urlopen(url).read()
        )
        redis_source.setex(key, 10, stream.getvalue())
    else:
        stream = BytesIO(file_stream)
    return stream
```






