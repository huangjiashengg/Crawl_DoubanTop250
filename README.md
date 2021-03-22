# 爬虫获取豆瓣Top250数据

## 前言

豆瓣Top250包含了豆瓣上口碑Top的电影，其中包含了其电影名称、海报、主演、导演以及相关语录等，同时也包括了电影主题、题材，类型，国家，评价人数，评分等信息。爬取的目的纯属为日常娱乐提供参考。

## 结论

本项目共爬取250条数据，每条数据即为一部电影，字段包含排名、电影名称、导演以及评分等；

项目对比了单进程与多进程方式的爬取效率，由于数据量较少，多进程爬取与单进程爬取效率差距并不明显；

项目分别采用了Redis作为数据缓存数据库和Excel表作为数据收集

## 技术实现过程

### 方式一

doubanTop250文件夹为scrapy框架爬取，并用Redis缓存，具体详见文档。

​							**Redis中一个数据条中的11个字段**

![结果1](C:\Users\DELL\PycharmProjects\doubanTop250\doubanTop250\README.assets\结果1.png)

​								**共250条数据，键值对**

![结果2](C:\Users\DELL\PycharmProjects\doubanTop250\doubanTop250\README.assets\结果2.png)

### 方式二

doubanTop250_1.0文件夹为requests+Beatifulsoup爬取，并做了单进程与多进程爬取效率测试

​								**Excel存储信息**

![结果3](C:\Users\DELL\PycharmProjects\doubanTop250\doubanTop250\README.assets\结果3.png)

## 交流

问题可留言2393946194@qq.com，欢迎互相学习交流