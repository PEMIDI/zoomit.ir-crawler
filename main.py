import requests
from bs4 import BeautifulSoup


def crawl_links():
    link = "https://www.zoomit.ir/tablet/page/2/"
    response = requests.get(link)

    soup = BeautifulSoup(response.text, 'html.parser')

    small_title_article = soup.find_all('a', attrs={'class': 'catlist__post-title'})
    small_title_articles = [li.get('href') for li in small_title_article]

    big_title_article = soup.find_all('div', attrs={'class': 'new-img'})
    big_title_articles = [li.a.get('href') for li in big_title_article]

    small_title_articles.extend(big_title_articles)

    print(len(small_title_articles))
    print(small_title_articles)


if __name__ == '__main__':
    crawl_links()
