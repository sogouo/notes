


gitlab 搭建过程

百度时对中国开发者最友好的搜索引擎，但是质量岑差不起；
强烈建议Google，买不起梯子，Bing 真是好东西！！

吐槽结束～～

一、安装与使用:
    
    参考文章, 讲解的非常全, 集合着看.
    How to Install GitLab on CentOS 7
    https://www.linuxcloudvps.com/blog/how-to-install-gitlab-on-centos-7/

    How To Install and Configure GitLab on CentOS 7
    https://linuxize.com/post/how-to-install-and-configure-gitlab-on-centos-7/

    注: 想给翻译下, 怎想英语渣的很，读起来都是靠翻译理解的😢



二、用本地的 Nginx 替换为 gitlab 内置Nginx
    
    原因:
        gitlab nginx 内置与本地 Nginx 端口冲突

        导致否则其他站点可能不能访问

    解决方案:
        方案一: 本地 Nginx 做代理转发到 gitlab nginx;
        方案二: 或者就直接用 本地 Nginx 访问

    Bing 一通搜索:


        方案一:

        gitlab nginx 端口监听修改
        $ sudo vim /etc/gitlab/gitlab.rb
            nginx['listen_port'] = 端口号
            external_url '域名'
        修改完成, 重启gitlab
        $ sudo gitlab-ctrl reconfigure

        添加 nginx 代理服务器配置

        ```nginx
            upstream  git{
                # 域名对应 gitlab配置中的 external_url
                # 端口对应 gitlab 配置中的 nginx['listen_port']
                server  域名:端口;
            }


            server{
                listen 80;
                # 此域名是提供给最终用户的访问地址
                server_name 域名;

                location / {
                    # 这个大小的设置非常重要，如果 git 版本库里面有大文件，设置的太小，文件push 会失败，根据情况调整
                    client_max_body_size 50m;

                    proxy_redirect off;
                    #以下确保 gitlab中项目的 url 是域名而不是 http://git，不可缺少
                    proxy_set_header Host $host;
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                    # 反向代理到 gitlab 内置的 nginx
                    proxy_pass http://git;
                    index index.html index.htm;
                }
            }
        ```
        参考
        https://segmentfault.com/a/1190000007661272

        gitlab 启用HTTPS：内容很多，在我看来不够清晰，一眼不到我想要
        http://www.cnblogs.com/roam/p/7678199.html

        方案二
        gitlab 使用现有 nginx 服务器
        https://www.liaohuqiu.net/cn/posts/non-bundled-web-server-for-gitlab/

        > 基本上参考该文档说明，感谢作者分享；发现很多人都转发(csdn)该文档
        > 不清楚该片是不是原创，支持原创
        
        问题:
            *959 connect() to unix:/var/opt/gitlab/gitlab-rails/tmp/sockets/gitlab.socket
            https://ruby-china.org/topics/5113
            原因是需要 socket 8
            https://yimity.com/2013/08/11/install-gitlab-questions.html

            http://www.cnblogs.com/lixiuran/p/6761299.html

            [crit] 20666#0: *9 connect() to unix:/var/opt/gitlab/gitlab-rails/tmp/sockets/gitlab.socket

            http://blog.51yip.com/server/1886.html **

            linux 查看nginx 启动用户
            使用ps aux | grep nginx命令，可以查找在运行的nginx的进程

            https://blog.csdn.net/mengzuchao/article/details/81170520


            SSL_do_handshake() failed (SSL: error:140770FC:SSL routines:SSL23_GET_SERV
            问题
                代理写成 https,应该是 http

            https://blog.csdn.net/enweitech/article/details/80847030

            SSL_do_handshake() failed (SSL: error:140770FC:SSL routines:SSL23_GET_SERVER_HELLO:unknown protocol
        https://blog.csdn.net/whing123/article/details/79382159

        会遇到: 权限问题

        

        其他参考
        https://www.jianshu.com/p/f64ccbb660ca

        
搜索词:
    gitlab nginx https 配置, gitlab nginx 配置

    https://segmentfault.com/markdown
    


