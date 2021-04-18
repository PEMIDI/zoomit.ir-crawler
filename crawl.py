import requests

import threading
from queue import Queue
from abc import ABC, abstractmethod
from parser import Parse
from utils import utils
class BaseCrawler(ABC):

    @staticmethod
    def get(url):
        
        response = requests.get(url)
        # when pagination is ending, zoomit.ir redirect the pages
        #   to another page,So I put a redirect checker
        if response.status_code == 200 and len(response.history) == 0:
            return response

        return None

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def save(self):
        pass

class LinkCrawler(BaseCrawler):
    
    def __init__(self):
        self.parser = Parse()
        

    def get_link(self, queue):

        while queue.qsize():
        
            page = queue.get()
            response = self.get(f"https://www.zoomit.ir/tablet/page/{page}/")
            print(f"Response status is {response}")
            print(len(response.history))
            print(f"Page : {page}")
            print("*"*10)
            queue.task_done()

    
    def get_pagination(self, category):
        response = self.get(f"https://www.zoomit.ir/{category}/")
        pagination_text = self.parser.pagination(response.text)
        
        return utils.pagination_text_parser(pagination_text)


    def start(self,category, threads=8):
        
        queue = Queue()
        for page in range(1, self.get_pagination(category)+1):
            queue.put(page)

        threads_list = []
        for _ in range(threads):
            x = threading.Thread(target=self.get_link, args=(queue, ))
            threads_list.append(x)
            x.start()

        for t in threads_list:
            t.join()

        print("Tasks Done")


    def save(self):
        pass

     




if __name__ == '__main__':
    get_links()