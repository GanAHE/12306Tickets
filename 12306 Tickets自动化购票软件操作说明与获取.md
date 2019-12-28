# **12306 Tickets version1.0 使用指南**

| 序号 |                           特别说明                           |
| :--: | :----------------------------------------------------------: |
|  1   |                  **本软件不具备抢票功能！！！**                  |
|  2   |        本软件只作为自动化工具，减少手动操作的繁琐！！        |
|  3   | 部分功能还需要完善，但由于当前事情较忙，<br />更新版本会相对较慢，开发队伍：@一直憨憨一直爽！<br /> @哈哈哈哈哈 @kgiu @GanAH @嗷呜不是喵呜！【都什么鬼昵称....】 |
|  4   | 核心代码参照GitHub大神的代码，经过简单修改，<br />加上GUI界面而得，参考代码地址：本项目开源地址：--> |
|  5   | 注意：当前仅支持Chrome浏览器，且仅支持chrome.78 及以上版本，若没有请在获取时选择相应的打包版本(chrome文件夹下)或是自行下载安装。 |

@[toc]
# 一. 功能说明

1. 实现12306自动化订票任务；
2. 可进行多人订票任务；
3. 采用Chrome浏览器插件执行，非脚本直接爬取进行post提交，相对安全；
4. 所有数据均不会保存，亦不会上传到云端，运行如有防火墙警告，为正常现象，确认使用即可，不会危害电脑安全，也不会窃取个人信息，可参见源代码。

**视频效果展示：**

# 二. 界面展示，安装说明及基本操作

操作界面如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191228104504573.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjY0NjEwMw==,size_16,color_FFFFFF,t_70#pic_center)

信息填写区域如下图，cookies的填写请往下查看：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191228104532549.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjY0NjEwMw==,size_16,color_FFFFFF,t_70#pic_center)

对于乘员信息，查看12306官网，如下图，比如：王大法，如果为学生，填写格式为王大法(学生)，注意为英文的括号：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191228104557157.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjY0NjEwMw==,size_16,color_FFFFFF,t_70#pic_center)
# 三. 特别操作及说明

## （一）.  关于cookies值的获取方式：

方法一（推荐） 复制如下代码：

![在这里插入图片描述](https://img-blog.csdnimg.cn/2019122810465060.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjY0NjEwMw==,size_16,color_FFFFFF,t_70#pic_center)
```py
None

```

方法二 （需要熟悉HTML的格式及网站源代码）Chrome

1. 定位到订票界面：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191228104710741.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjY0NjEwMw==,size_16,color_FFFFFF,t_70#pic_center)

2. 点击F12,弹出如下窗口：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191228104712965.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjY0NjEwMw==,size_16,color_FFFFFF,t_70#pic_center)

3. 接下来的操作步骤如下图中标识：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191228104826373.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjY0NjEwMw==,size_16,color_FFFFFF,t_70#pic_center)

4. jc_save_fromstation的Value填入始发站cookies，jc_save_tostation填入终点站cookies,此时可以顺便计下需要指定列车对应的从上到下的序号，或是不指定由软件自动选择。

## **（二）. 关于邮件通知系统的登录授权码获取**

目前仅支持QQ邮箱系统，后续将会添加网易163系统。

> 特别说明：添加邮箱不需要邮箱的账户密码，只需授权码即可，保护邮箱安全！

具体获取授权码方法：

登录网页版QQ邮箱，找到：设置-账户-POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务，生成授权码，填入即可。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191228104857721.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjY0NjEwMw==,size_16,color_FFFFFF,t_70#pic_center)

## （三）. 关于Chrome版本信息查看问题

1. 打开chrome，找到右上角并执行图示操作：

 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20191228105007267.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjY0NjEwMw==,size_16,color_FFFFFF,t_70#pic_center)

2. 打开即可看到当前的Chrome版本信息，软件当前支持78.0以上版本。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191228104937808.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjY0NjEwMw==,size_16,color_FFFFFF,t_70#pic_center)

# 四. 新版本更新及发布获取渠道

| 渠道一 | 微信公众号：[点击](https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzUxNDkyMTQ1Nw==&scene=126&bizpsid=1558318813#wechat_redirect) |
| ------ | ------------ |
| 渠道二 | GitHub仓库：[**点击**](https://github.com/GanAH/12306Tickets) |

微信公众号后台回复：Ticket即可，此时会返回几个下载链接，自行选择便好。

# 五. 当前版本特性

1. 可订票时间限制到2月29日；
2. 采用浏览器插件实现模拟操作；
3. 可进行邮箱通知；
4. 座位选择；
5. 多人同时选座（12306账户下需要有该乘员的信息）。

# 六. 预期新版本特性（不定时更新，大概）

1. 耗时监测，完善监测信息，定位错误源，确保软件稳定性；
2. 定时订票（自动识别验证码，当前未完成，需手动点击），邮件通知；
3. 界面美化（任务逻辑完成后）；
4. 防反爬；
5. 多线程监测与订票；
6. PC端迁移到移动端，实现云端挂载订票（可能）；
件稳定性；
7. 定时订票（自动识别验证码，当前未完成，需手动点击），邮件通知；
8. 界面美化（任务逻辑完成后）；
9. 防反爬；
10. 多线程监测与订票；
11. PC端迁移到移动端，实现云端挂载订票（可能）；
12. .......（肯定还有，但没想好——）

七. 微信公众号【合作】
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191228105128547.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjY0NjEwMw==,size_16,color_FFFFFF,t_70#pic_center)
