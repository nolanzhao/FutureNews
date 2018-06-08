# --*-- coding: utf-8 --*--
import os
import sys
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(BASE_DIR)
import time
import random
from news_crawler.media_config import MEDIA as media_list
from news_crawler.crawler import crawl
from settings import CRAWL_INTERVAL


def start():
    random.shuffle(media_list)
    for m in media_list:
        for k, v in m.items():
            source = k
            for category, url in v.items():
                print("######", source, category, url, "######")
                crawl(url, source, category)
                print("\n")






if __name__ == '__main__':
    while True:
        start()
        time.sleep(60 * CRAWL_INTERVAL)
