<center> <h2>网络设备性能监测与管理系统</h2></center>



## 主要技术

- 后端：
    - 确定：
        - Server : Flask , Telegraf , Psutil 
        - Agent : Telegraf , Psutil 
    - 待定：
        - 性能相关 : Snmp 
        - 网络相关 : Scapy , Npcap ( Windows ) , TCPdump ( Linux )
- 前端：
    - 确定：Vue
- 数据库：InfluxDB、MongoDB

## 架构

<img src="https://gitee.com/hanmengnan/images-of-notes/raw/master//notes/image-20201219112401641.png" alt="image-20201219112401641" style="zoom:50%;" />





架构主要由 Server 端与 Agent 端组成：

- Server : 
    - 暂用：
        1. 利用 **Flask** 框架搭建 Web 服务器功能，起数据展示功能，同时本机也作为一台 Agent 采集数据。
        2. 利用 **MongoDB** 作为辅助数据库，存储其他数据。 
    - 考虑：换用 **Go** 语言相关的 Web 框架。
- Agent : 
    - 确定：主要利用 **Telegraf** , 辅以 **Python 编写的 Psutil 脚本** 采集本机性能数据 ，存入 **InfluxDB** 与 **MongoDB** 。
    - 待定：是否在数据输出时加入聚合插件。



## 功能

### 登录

### 监控

- 系统信息

    - CPU
        - 型号
        - 核心数
        - 占用率
        - 进程数
    - 磁盘
        - 磁盘容量
        - 可用空间
        - 占用率
        - IO次数
        - IO数据量
    - 内存
        - 内存大小
        - 占用率
        - 虚拟内存
        - Cache大小
    - 网络
        - 时延
        - 带宽
        - 丢包率
        - IP
        - TCP
        - UDP
    - 进程
        - 进程名称
        - 内存使用率
        - CPU使用率
        - 图表

- 服务器

    - NGINX
    - Apache
    - Tomcat

- 数据库

    - MySQL
    - SQL Server
    - Redis

- 容器

    - Docker
    - K8s

- 端口监控

    - 状态

    - 进程

- 接口监控

### 展示看板

- 大屏展示

- 公众展示

### 日志

- 记录

- 分析

### 预警

### 拓扑图

