常用Linux 命令
以ubuntu, centos 环境

1.关机、重启
    关机: sudo shutdown -h now
    重启: sudo reboot

2.查看端口以及使用情况
    环境ubuntu 环境下
    a.查看TCP 或者 UDP 端口使用情况, 命令如下:
    $ sudo netstat -anp
    
    b.使用lsof 命令查看具体端口信息，例如属于那个应用程序
    $ sudo lsof -i :3306
    
    c.查看已激活Internet连接(仅服务器)端口使用情况
    $ netstat -tln

    
3.Ubuntu LNMP 以及 nginx + uwsgi + Django 环境搭建(初学者入门基础教程)
http://wiki.ubuntu.org.cn/Nginx#.E5.AE.89.E8.A3.85nginx

我目前ubuntu 版本如下
图例
<img src='' >
安装方式是通过 sudo apt-get install nginx

在该系统版本下，需要订正一个错误
"所有的配置文件都在/etc/nginx下，并且每个虚拟主机已经安排在了/etc/nginx/sites-available下"
修改为
"所有的配置文件都在/etc/nginx下，并且每个虚拟主机已经安排在了/etc/nginx/sites-enabled/*下"

图例如下
<img src='' >

