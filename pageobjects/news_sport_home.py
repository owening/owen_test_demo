#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 14:34
# @Author  : owen
# @File    : news_sport_home.py

from framework.base_page import BasePage

class SportNewsHomePage(BasePage):
    #NBA入口
    nba = "xpath=>//*[@id='col_nba']/div[1]/div[2]/ul[1]/li[1]/a"

    def click_nba_link(self):
        self.click(self.nba)
        self.sleep(2)