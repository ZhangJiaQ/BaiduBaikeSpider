import urlparse
import re
from bs4 import BeautifulSoup


class HtmlParser(object):


    def parse(self,page_url,html_content):

        if page_url is None or html_content is None:
            return

        soup = BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')
        new_urls = self.__get_new_urls(page_url,soup)
        new_data = self.__get_new_data(page_url,soup)
        return new_urls,new_data

    def __get_new_data(self, page_url, soup):
        #<dd class="lemmaWgt-lemmaTitle-title">  <h1>Python</h1>
        #<div class="lemma-summary" label-module="lemmaSummary">

        res_data = {}
        res_data['url'] = page_url

        title_data = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_data.get_text()

        summary_data = soup.find('div',class_='lemma-summary')
        res_data['summary'] = summary_data.get_text()
        return res_data

    def __get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/item/'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        return new_urls