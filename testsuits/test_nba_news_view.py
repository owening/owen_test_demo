#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 15:11
# @Author  : owen
# @File    : test_nba_news_view.py

import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import BaiduHomePage
from pageobjects.baidu_news_home import NewsHomePage
from pageobjects.news_sport_home import SportNewsHomePage

class ViewNBANews(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_view_nba_views(self):
        #初始化百度首页，并点击新闻链接
        baiduhome = BaiduHomePage(self.driver)
        #baiduhome.click_news()
        self.driver.find_element_by_xpath("//a[@class='mnav' and contains(text(),'新闻')]").click()
        #初始化一个百度新闻主页对象，点击体育
        newshome = NewsHomePage(self.driver)
        #newshome.click_sports()
        self.driver.find_element_by_xpath("//*[@id='channel-shanghai']/div/ul/li[7]/a[contains(text(),'体育')]").click()
        #初始化一个体育新闻主页，点击NBA
        sportnewhome = SportNewsHomePage(self.driver)
        #sportnewhome.click_nba_link()
        self.driver.find_element_by_xpath("//*[@id='col_nba']/div[1]/div[2]/ul[1]/li[1]/a").click()
        sportnewhome.sleep(3)
        sportnewhome.get_windows_img()
        sportnewhome.sleep(6)

if __name__ == '__main__':
    unittest.main()

