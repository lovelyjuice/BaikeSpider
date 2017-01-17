# -*- coding:utf-8 -*-
"""
Created on Dec 24, 2016

@author: wqh11
"""


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    pass

    def add_new_url(self, url):
        if url is None:
            return
        if (url not in self.new_urls) and (url not in self.old_urls):
            self.new_urls.add(url)
        return

    pass

    def has_new_url(self):
        return len(self.new_urls) != 0

    pass

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    pass

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        else:
            for aaa in urls:
                if (aaa not in self.new_urls) and (aaa not in self.old_urls):
                    self.new_urls.add(aaa)
        pass
