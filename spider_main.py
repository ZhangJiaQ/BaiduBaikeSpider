# coding:utf8
from BaiduSpider import url_manager, html_parser, html_downloader, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.parser = html_parser.HtmlParser()
        self.downloder = html_downloader.HtmlDownloader()
        self.outputer = html_outputer.HtmlOutputer()

    def carw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()######
                print "craw %d,%s"%(count,new_url)
                html_content = self.downloder.download(new_url)
                new_urls , new_data = self.parser.parse(new_url , html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count += 1
                if count == 1000:
                    break
            except:
                print "craw wrong"

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.carw(root_url)