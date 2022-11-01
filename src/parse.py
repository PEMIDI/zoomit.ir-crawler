from bs4 import BeautifulSoup
import requests


class Parse:

    @staticmethod
    def link_parser(response):
        soup = BeautifulSoup(response.text, 'html.parser')

        article_divs = soup.find_all('a', attrs={'class': 'catlist__post-title'})
        article_links = [li.get('href') for li in article_divs]

        # some articles in zoomit.ir has difference is size
        #    So they need another parser
        wide_row_div = soup.find_all('div', attrs={'class': 'new-img'})
        wide_row_articles = [li.a.get('href') for li in wide_row_div]

        article_links.extend(wide_row_articles)
        return list(article_links)

    @staticmethod
    def pagination(html_doc):

        soup = BeautifulSoup(html_doc, 'html.parser')
        pagination_tag = soup.find('div', attrs={'class': 'col-md-3 pad15T pad15B hidden-xs'})
        return pagination_tag.text

    @staticmethod
    def article_parser(response):
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.h1
        if title:
            title = title.text

        body = soup.find('div', attrs={'class': 'article-content'})
        if body:
            body = body.text

        posted_datetime = soup.find('div', attrs={'class': 'author-details-row2'})
        if posted_datetime:
            posted_datetime = posted_datetime.text

        author_name = soup.find('span', attrs={'class': 'color-red'})
        if author_name:
            author_name = author_name.text

        return {
            'title': title, 'body': body,
            'posted_datetime': posted_datetime, 'author': author_name
        }

    def sample_article(self):
        response = requests.get('https://www.zoomit.ir/car-news/370023-genesis-electrified-g80/')

        return self.article_parser(response)


if __name__ == '__main__':
    crawler = Parse()
    print(crawler.sample_article())
