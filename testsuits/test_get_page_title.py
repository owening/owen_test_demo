#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 16:40
# @Author  : owen
# @File    : test_get_page_title.py

import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import BaiduHomePage

class GetPageTitle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_title(self):
        homepage = BaiduHomePage(self.driver)
        print(homepage.get_page_title())

