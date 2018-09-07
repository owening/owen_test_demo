#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 16:18
# @Author  : owen
# @File    : baidu_homepage.py

from framework.base_page import BasePage

class BaiduHomePage(BasePage):

    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"
    news_link = "xpath=>//a[@class='mnav' and contains(text(),'新闻')]"   #点击百度新闻首页入口

    def input_search(self,text):
        self.input(self.input_box,text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

    def click_news(self):
        self.click(self.news_link)
        self.sleep(2)

