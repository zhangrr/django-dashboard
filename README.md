django-dashboard 虚机生产系统
=============================

环境说明
--------
### 用到了django、celery、rabbitmq、mysql、highcharts、bootstrap。<br/><br/>

### 前端采用django，适用于中小型系统，且组件丰富，不用重复造轮子，承载10-40人的使用应该没问题。<br/>
### 中间件采用rabbitmq消息系统，已删除缺省的配置，也是可以平行拓展，增加node，可以承载海量消息。<br/>
### celery异步系统，用来异步执行任务。<br/>
### highcharts用户动态展示数据。<br/>

### 后面创建虚机可以采用两种方法：<br/>
### 一、用celery的worker，定时或者分批的调用saltstack的api，生产虚机。<br/>
### 　　调用saltsatck的方法也有两种：<br/>
### 　　①django和salt-master在同一台机器上，直接调用salt-api<br/>
### 　　②django和salt-master不在同一台机器上，在salt-master上面用flask封装一个http接口，带token认证，django远程调用。<br/><br/>

### 二、用kombu框架直接把创建虚机的消息放进rabbitmq，然后客户端写个pika的程序接收消息生产虚机。<br/><br/>

### 数据库的部分基本使用orm的映射，没有sql代码在里面，不过orm的语法也需要了解。<br/>
### view部分严格采用mvc，用bootstrap的weight对各个输入控件进行控制。<br/>
### highchart部分由于是要采取数据的序列，跟orm实在没有什么关系，强行套入orm很生硬，所以采用直接sql得到数据的方法。<br/>
### 用celery异步执行任务的话，用ajax来查询状态，动态更新任务的状态。<br/>

django-dashboard 虚机生产系统
-----------------------------
![主页](http://www.linuxboy.net/appimgs/django01.jpg)
![主页](http://www.linuxboy.net/appimgs/django02.jpg)
![主页](http://www.linuxboy.net/appimgs/django03.jpg)
![主页](http://www.linuxboy.net/appimgs/django04.jpg)

django-dashboard部署
--------------------
### rabbitmq部署<br/>
### django部署<br/>
### supervisord部署<br/>
### 请自行查阅文档，不累述了。<br/>

