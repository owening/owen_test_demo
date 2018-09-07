#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 14:33
# @Author  : owen
# @File    : baidu_news_home.py

from framework.base_page import BasePage

class NewsHomePage(BasePage):
    #点击体育新闻入口
    sport_link ="xpath=>//*[@id='channel-shanghai']/div/ul/li[7]/a"

    def click_sports(self):
        self.click(self.sport_link)
        self.sleep(2)