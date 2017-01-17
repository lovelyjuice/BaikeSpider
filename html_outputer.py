# -*- coding:utf-8 -*-
"""
Created on Dec 24, 2016

@author: wqh11
"""


class HtmlOutputer(object):
    def __init__(self):
        self.data = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.data.append(new_data)

    pass

    def print_html(self):
        f = open(r"D:\Baike.html", "w+")
        f.write("<html><head><meta charset=\"utf-8\"><title>BaikeCrawl</title></head><body>")
        for temp in self.data:
            print temp["title"]
            f.write("%s<br>" % temp["title"])
            f.write("%s<br><br>" % temp["sum"])
        f.write("</body></html>")
        pass
