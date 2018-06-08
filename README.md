# FutureNews

#### 1. 创建数据库
```
mysql> create database future_news default charset utf8;
```

#### 2. 配置settings.py
抓取媒体的配置在news_crawler/media_config.py

#### 3. 运行爬虫
```python
python news_crawler/main.py
```

#### 4. 运行web
```python
python web/app.py
```