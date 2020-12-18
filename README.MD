<center> <h2>网络设备性能监测与管理系统</h2></center>



## 主要技术

- 后端：
    - 确定：Flask、Psutil
    - 待定：Scapy、Snmp、Npcap（Windows）、TCPdump（Linux）
- 前端：
    - 确定：Vue

## 架构

<img src="https://gitee.com/hanmengnan/images-of-notes/raw/master//notes/image-20201218223347229.png" alt="image-20201218223347229" style="zoom:50%;" />





架构主要由Server端与Agent端组成：

- Server：负责收集Agent端的数据，同时本机也作为一台Agent设备收集数据。将搜集到的数据，以WEB可视化形式展示。
- Agent：负责获取本机数据，并将其作为“Server的请求”的回复提供给Server。



## 功能

### 登录

### 设备监控

1. 设备列表

2. 可以手动添加设备
3. 设备种类、名称、位置、运行时间

### 进程监控

1. 进程名称
2. 内存使用率
3. CPU使用率
4. 图表

### 端口监控

1. 状态
2. 进程

### Docker 监控

### 接口监控

### 展示看板

1. 大屏展示
2. 公众展示

### 硬件性能详情

1. CPU
    1. CPU百分比
    2. 核心数
    3. 型号
    4. 进程数
2. 内存
    1. 内存大小
    2. 占用率
    3. 虚拟内存
3. 磁盘
    1. 磁盘容量
    2. 可用空间
    3. 占用率
    4. IO次数
    5. IO数据量

### 网络性能详情

1. 概览
    1. 时延
    2. 带宽
    3. 丢包率
2. 详情
    1. IP
    2. TCP
    3. UDP

### 日志

1. 记录
2. 分析

### 预警

### 拓扑图

