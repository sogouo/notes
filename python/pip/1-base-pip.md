
Python pip 安装与使用

pip 是 Python 包管理工具, 该工具提供了对 Python 包的查找、下载、安装、卸载的功能

从 Python 2.7.9+ 或者 Python 3.4+ 以上版本都自带 pip 工具

pip 官网
https://pypi.org/project/pip/


可以通过以下命令来判断是否已经安装:
$ pip --version

如果未安装，可以手动安装
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ sudo python get-pip.p
或者
$ sudo python3 get-pip.py

用哪个版本的 Python 运行安装脚本，pip 就被关联到哪个版本，如果是 Python3 则执行以下命令：

一般情况 pip 对应的是 Python 2.7，pip3 对应的是 Python 3.x


部分 linux 发行版可以直接用包管理器安装pip, 如果 Debian 或者 Ubuntu
sudo apt-get install python-pip



pip 常用命令
1.查看版本或者路径
    $ pip --version

2.获取帮助
    $ pip --help

3.升级
    $ pip install -U pip
    或者
    $ pip install --upgrade pip

4.安装包
    # 安装最新版本
    $ pip install PackageName

    # 指定版本
    $ pip install PackageName=1.2

    # 最小版本
    $ pip install 'PackageName>=1.2'

5.升级包
    $ pip install --upgrade PackageName
    升级指定的包，通过使用==, >=, <=, >, < 来指定一个版本号。

6.卸载包
    $ pip uninstall PackageName

7.搜索包
    $ pip search PackageName

8.显示安装包信息
    $ pip show PackageName

9.显示指定包都详情
    $ pip show -f PackageName

10.列出已安装的包
    $ pip list

11.查看可升级的包
    $ pip list -0




参考: http://www.runoob.com/w3cnote/python-pip-install-usage.html
