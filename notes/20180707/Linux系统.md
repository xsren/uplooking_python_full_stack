
Centos-7.0-x86_64操作系统



# Linux安装

## 安装virtualbox

[https://www.cnblogs.com/york-hust/archive/2012/03/29/2422911.html](https://www.cnblogs.com/york-hust/archive/2012/03/29/2422911.html)


选择硬盘，设置root用户密码。

## 安装系统

```
cat /etc/redhat-release  查看系统版本
yum update -y            更新所有软件
yum install -y net-tools 安装网络包
```

```
ifconfig命令找不到
　　1、打开 vi /etc/sysconfig/network-scripts/ifcfg-eth0
（每个机子都可能不一样，但格式会是“ifcfg-eth数字”），
把ONBOOT=no，改为ONBOOT=yes

　　2、重启网络：service network restart
　　
遇到了在桥接地址下无法获取IP的问题：
解决方法有两个：
1、直接配置IP
GATEWAY=255.255.255.0
IPADDR=172.25.3.X
PREFIX=24
DNS1=202.106.0.20
DNS2=114.114.114.114
2、补全缺少的文件
cd /etc/udev/rules.d/
70-persistent-net.rules
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="08:00:27:b4:6b:e1", KERNEL=="eth*", NAME="enp0s3"

其中"08:00:27:b4:6b:e1"是物理机的MAC地址
```

```
putty或者xshell  可以远程登录linux机器
winscp 或者 xftp  可以往远程机器拷贝文件
yum install -y lrzsz
sz 下载
rz 上传

MAC 下：
ssh root@172.25.3.32
```

# Linux使用

[ yum  http://www.runoob.com/linux/linux-yum.html](http://www.runoob.com/linux/linux-yum.html)



```
vi 命令

Tab 补全
使用光标移动
按“i”进入编辑模式
按“ESC”退出
按“:”,再按“w”表示保存，“q”表示退出。
```

# Linux常用命令
[https://blog.csdn.net/ljianhui/article/details/11100625](https://blog.csdn.net/ljianhui/article/details/11100625)

```
cd 进入指定目录
ls 或者 ll 查看目录文件
pwd 查看当前路径
grep 匹配文本
grep 'a' -r -n test.py 
cp (-r 拷贝文件夹)   拷贝文件或者目录
mv   移动文件或者目录
rm 删除
ps 查看进程
ps -ef | grep python
kill -9 PID PID是程序进程号
file 判断文件类型

tar czvf test.tar.gz test 压缩gz
tar xzvf test.tar.gz 解压缩gz
yum -y install bzip2 安装bzip2库
tar -jcv -f test.tar.bz2 test 压缩bz2
tar -jxv -f test.tar.bz2 -C . 解压bz2

cat 打印文本内容到屏幕

chown -R xsren test.py 更改文件用户

chmod +x test.py 修改文件权限

time 计算程序运行时间

date 显示机器时间


```


# Python开发环境

pycharm

需要安装python2

```
需要更改pip源

MAC :
mkdir .pip
vim .pip/pip.conf
写入以下内容：

[global]
index-url = https://pypi.douban.com/simple

Windows:
在 C:\Users\{当前用户名}下新建pip文件夹
然后在pip文件夹下新建pip.ini文件，写入源：

```