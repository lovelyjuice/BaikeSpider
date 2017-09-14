# -*- coding:utf-8 -*-
"""
Created on Dec 24, 2016

@author: wqh11
"""
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        raw_urls = soup.find_all("a", href=re.compile(r"/item/"))
        for temp in raw_urls:
            full_url = urlparse.urljoin(page_url, temp["href"])
            new_urls.add(full_url)
        return new_urls

    pass

    def _get_data(self, page_url, soup):
        res_data = {}
        # <dd class="lemmaWgt-lemmaTitle-title">
        title = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find("div", class_="lemma-summary")
        res_data["title"] = title
        res_data["sum"] = summary_node
        res_data["url"] = page_url
        return res_data

    pass

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return None
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url, soup)
        data = self._get_data(page_url, soup)
        return new_urls, data

    pass
