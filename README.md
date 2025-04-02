# BatchCleanGiteaUsers
Resolve the issue of Gitea Git servers being released on the external network, where public registration was not closed, resulting in someone using scripts to register a large number of useless accounts and repositories. It is now necessary to delete these accounts and repositories in bulk

我用gitea搭建了一个内部使用的代码管理服务器，并发布在公网上，突然有一天，被人用脚本注册了大量无用的账号和仓库，导致服务器被大量用户访问，我需要批量删除这些账号和仓库，但是gitea并没有提供批量删除账号和仓库的功能，所以只能手动删除了。
本代码是为了解决发布在外网的Gitea git 服务器，因为没有关闭公开注册，导致有人用脚本注册了大量无用的账户和仓库，现需要批量删除这些账号和仓库的情况

在命名用时，注意修改代码的 excludeUsers = ["user1","user2",	"user3", "user4"]  # 排除用户列表，将要保留的用户名称放在这里，将自己要保留的用户放在这里

使用方式：安装python 3.8以上版本，然后执行python main.py 即可