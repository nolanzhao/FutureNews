from pytz import timezone


# MongoDB
DB_PARAM = {
    'database': 'future_news',
    'ip': '127.0.0.1',
    'port': 27017,
    'username': "",
    'password': "",
}


# 新闻抓取频率(分钟)
CRAWL_INTERVAL = 120


# TimeZone
UTC = timezone('UTC')
TIMEOUT = 60