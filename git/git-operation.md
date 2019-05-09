日常操作

git 仓库地址替换

例如: repository1

# 删除本地仓库远程地址
> git remote remove origin 

# 添加新仓库地址
> git remote add origin https://github.com/xxx/xxx.git

# 将本地地址推送到新仓库地址
> git push origin master


# 创建分支
> git branch -


# 从 master 创建分支

> git fetch origin master:dev
> git checkout dev
> git push origin dev



gitlab 或者github 使用过程总结


具体文档:

github 或者 gitlab 通过 ssh 方式拉取或者推送

	https://gitlab.shinephp.cn/help/ssh/README#generating-a-new-ssh-key-pair

	生成 SSH ED25519 Key 方便操作

	ssh-keygen -t ed25519 -C "email@example.com"

	或者用户 RSA
	ssh-keygen -o -t rsa -b 4096 -C "email@example.com"

	-> 保存路径
	~/.ssh/id_ed25519.pub

	-> 将 ssh key 写入到 gitlab 或者github
	gitlab > setting > ssh key > 


gitlab 或者 github 从 A 用户下B仓库(或者项目) fork 自己(C)的 D 仓库(项目)下

会涉及到B，D的更新和更新

合并
	D -> B: D 仓库的更新直接推送到B 项目，需要发起 PR (New pull request)

更新
	B -> D: 将 B 最新代码同步到D仓库中, 需要在 D 本地仓库下，增加 B 远程连接

	git remote add upstream B
	git pull upstream <branch-name>




