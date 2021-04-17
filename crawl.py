import requests
from bs4 import BeautifulSoup


def get_links():
    crawl = True
    links = list()
    pagination = 92

    while crawl:
        url = f"https://www.zoomit.ir/tablet/page/{pagination}/"
        response = requests.get(url)
        if len(response.history) > 0:
            return None

        print(f"crawling page: {pagination}")

        soup = BeautifulSoup(response.text, 'html.parser')
        article_divs = soup.find_all(
            'a', attrs={'class': 'catlist__post-title'}
        )
        article_links = [li.get('href') for li in article_divs]
        wide_row_div = soup.find_all('div', attrs={'class': 'new-img'})
        wide_row_articles = [li.a.get('href') for li in wide_row_div]

        article_links.extend(wide_row_articles)
        print(len(article_links))
        print(article_links)
        pagination += 1
        links.extend(article_links)

    return links

def get_articles(url):
    pass
    # response = requests.get(url)
    # if response.status_code == 200:
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     title = find_


    # soup = BeautifulSoup()

if __name__ == '__main__':
    get_links()