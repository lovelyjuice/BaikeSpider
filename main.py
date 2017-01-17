# -*- coding:utf-8 -*-
"""
Created on Dec 24, 2016

@author: wqh11
"""
import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.html_downloader = html_downloader.htmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    pass

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 0
        while self.urls.has_new_url() and count < 200:
            try:
                new_url = self.urls.get_new_url()
                html_cont = self.html_downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count += 1
                print "crawl %d times" % count
            except:
                print "crawl failed"
        pass
        self.outputer.print_html()
        pass

    pass

    def start(self):
        new_url = self.urls.get_new_url()
        html_cont = self.html_downloader.download(new_url)
        new_urls, new_data = self.parser.parse(new_url, html_cont)
        self.urls.add_new_urls(new_urls)
        self.outputer.collect_data(new_data)
        pass


if __name__ == '__main__':
    root_url = "http://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
