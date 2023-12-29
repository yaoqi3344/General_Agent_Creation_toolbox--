# General_Agent_Creation_toolbox
  ***General_Agent_Creation_toolbox***收集AI开发用工具，用于简单，有效的创建网络部署用AI Agent。

   >*数据收集*：爬虫工具/语料库整理
  
  
   >*开发教程*：开发工具源码/开发工具文本教程/基础模板/markdown语法教程/教程视频
  
  
   >*管理组件*：注册-登陆/微信-支付宝-微博等SDK/redis缓存/mysql历史消息储存

 
   >*测试组件*：语言模型测试工具/网站运行性能工具/网络测试工具/云服务器配置检测
  

   >*部署工具*：部署脚本/网关-域名-服务器教程/https修改工具
  
  
   >*运维工具*：日志收集平台/数据库管理/性能检测
  
  
   >*宣传模板*：小红书/抖音/微博/微信公众号 运营教程/撰写模板
  
  
## 爬虫工具
网络爬虫，有时称为蜘蛛或spiderbot，通常简称为crawler，是一种系统地浏览万维网的互联网机器人，通常由搜索引擎操作，用于网络索引(网络爬虫)。

>Github topic:https://github.com/topics/crawler
>
>A Web crawler, sometimes called a spider or spiderbot and often shortened to crawler, is an Internet bot that systematically browses the World Wide Web and that is typically operated by search engines for the purpose of Web indexing (web spidering).

### Easycrawler:
https://blog.csdn.net/Pluviophiles/article/details/130734349

>使用场景：```新手/小白简单抓取``` ```论坛文本信息``` ```使用python```
>
>使用方法：
```python3 Crawler.py```
```python3 DelKeyWord.py```

### Easyspider：
https://github.com/NaiboWang/EasySpider

>使用场景：```复杂场景-精确信息``` ```网页图形化抓取```
>
>[下载](https://www.easyspider.cn/files/v0.6.0/)
>[使用方法](https://github.com/NaiboWang/EasySpider/wiki)


### ~~Diffbot~~ 
https://www.diffbot.com/products/extract/testdrive/

>使用场景：```只输入URL，不编码``` ```结构化信息``` ```2周免费``` ```工作邮箱```
>
>[下载](https://app.diffbot.com/get-started/)


## 语料库
语料库指经科学取样和加工的大规模电子文本库，其中存放的是在语言的实际使用中真实出现过的语言材料。


### 语料库检索平台

https://languageresources.github.io/

>使用场景：```2018年之前发布的语料库``` ```国内整理的语料库```

### huggingface datasheet

https://github.com/huggingface/datasets

>使用场景：```发布/抓取huggingface上的datasheet```
>
>使用方法：```pip install datasets```

### 本地代码包含
从Meta ParlAI 项目：

PersonaChat, DailyDialog, Wizard of Wikipedia, Empathetic Dialogues, SQuAD, MS MARCO, QuAC, HotpotQA, QACNN & QADailyMail, CBT, BookTest, bAbI Dialogue tasks, Ubuntu Dialogue, OpenSubtitles, Image Chat, VQA, VisDial and CLEVR.

[全部](https://github.com/facebookresearch/ParlAI/blob/main/parlai/tasks/task_list.py) 

#### Wizard of Wikipedia
https://github.com/facebookresearch/ParlAI/tree/main/projects/wizard_of_wikipedia

>使用场景：```通用模型训练``` ```教师和学徒的对话``` ```包括 22311 个对话和 201999 个语句，平均每个对话包含 9 个语句。```
>
>[使用方法](https://github.com/facebookresearch/ParlAI/tree/main/projects/wizard_of_wikipedia)

#### OpenWebText
https://skylion007.github.io/OpenWebTextCorpus/

>使用场景：```通用模型训练``` ```reddit仿照Openai GPT2``` ```40GB```
>
>下载：https://drive.google.com/drive/folders/1IaD_SIIB-K3Sij_-JjWoPy_UrWqQRdjx

## 管理组件
管理组件用于网络部署的AI Agent实现：登陆-注册-数据库表单

### 微信jssdk
https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/JS-SDK.html

>使用场景：```登陆验证``` ```微信支付```
>
>[下载](http://res.wx.qq.com/open/js/jweixin-1.6.0.js)
>[使用](https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/JS-SDK.html)

### 支付宝SDK

>使用场景：```登陆验证``` ```支付宝支付```
>
>下载：[APP端口](https://opendocs.alipay.com/open/04km1h ) [服务端口](https://opendocs.alipay.com/open/54/106370)
>
>[使用](https://opendocs.alipay.com/support/01rfry)

## 测试组件
用于再部署前后测试AI agent性能：生成的回答-运行性能-负载测试

### evals
https://github.com/openai/evals

>使用场景：```语言模型评估框架``` ```测试模板撰写```
>
>下载：
>
```
cd evals
git lfs fetch --all
git lfs pull
```
>
>[使用](https://github.com/openai/evals/blob/main/docs/build-eval.md)

### Trulens
https://github.com/truera/trulens

>使用场景：```RAG语言模型回答评分框架``` ```Honest, Harmless and Helpful Evaluations```
>
>下载：```pip install trulens-eval```
>
>[使用](https://www.trulens.org/trulens_eval/quickstart/)https://www.trulens.org/trulens_eval/quickstart/

### JMeter
https://github.com/apache/jmeter

> 使用场景：```网页负载测试``` ```java```
>
> [下载](https://jmeter.apache.org/download_jmeter.cgi)
> [使用](https://jmeter.apache.org/)

### selenium
https://www.selenium.dev/

> 使用场景：```基于浏览器的回归自动化套件和测试```
>
> [下载](https://www.selenium.dev/downloads/)
> [使用](https://www.selenium.dev/documentation/)


## 部署工具
用于部署网站在云服务器上

### nginx

### certbot
https://certbot.eff.org/

>使用场景：```免费网络证书下载管理``` ```HTTPS``` ```Let's Encrypt```
>
>下载：```sudo apt install certbot python3-certbot-nginx``` ```certbot --nginx```

### docker

## 运维工具
用于收集日志，管理错误信息，清理内存垃圾

### Loki
https://github.com/grafana/loki/

>使用场景：```日志收集``` ```预警``` ```数据展示```
>
>[下载](https://grafana.com/docs/loki/latest/setup/install/)
>[使用](https://grafana.com/docs/loki/latest/get-started/)


## 宣传模板




