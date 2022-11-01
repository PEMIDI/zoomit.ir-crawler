

import threading
import sys

from crawl import LinkCrawler, ArticleCrawler
from models.initiate_db import create_table
from queue import Queue
from utils.constants import CATEGORIES
from utils.utils import category_exist



def initiate_database():
    create_table()


if __name__ == '__main__':

    if sys.argv[1] == 'show_categories':
        # crawler = ArticleCrawler()
        categories = CATEGORIES
        for cat in categories:
            print(f"{categories.index(cat)} : {cat['name']}")



    if sys.argv[1]  == 'crawl':
        if category_exist(sys.argv[2]):
            create_table()
            print('models created')
            print('category found, is crawling...')
            crawler = LinkCrawler()
            crawler.start(category=sys.argv[2])
            print('crawl ended')
        else:
            print('category not found!')
            
            




    if sys.argv[1] == 'get_article':
        if category_exist(sys.argv[2]):
            print('hello')
            crawler = ArticleCrawler()
            crawler.start(category=sys.argv[2])
        
    if 'get_articles':
        pass
        # crawler = ArticleCrawler()
        # # # # url = 'https://www.zoomit.ir/tablet/369941-samsung-galaxy-tab-a7-lite-silver-render/'
        # crawler.create_categoreis()
    