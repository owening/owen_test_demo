#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 16:15
# @Author  : owen
# @File    : browser_engine.py

import ConfigParser
import os
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getLog()

class BrowserEngine(object):

    dir = os.path.dirname(os.path.abspath('.'))  #注意相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    firefox_driver_path = dir + '/tools/geckodriver.exe'

    def __init__(self,driver):
        self.driver = driver

    #从config.ini读取浏览器类型,返回驱动
    def open_browser(self,driver):
        config = ConfigParser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType","browserName")
        logger.info("您已经选择了 %s 浏览器." % browser)
        url = config.get("testServer","URL")
        logger.info("测试url是: %s" %url)

        if browser == "Firefox":
            driver = webdriver.Firefox(self.firefox_driver_path)
            logger.info("驱动Firefox浏览器.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("驱动Chrome浏览器.")
        elif browser == "IE":
            driver = webdriver.Ie()
            logger.info("驱动IE浏览器.")

        driver.get(url)
        logger.info("打开站点: %s" %url)
        driver.maximize_window()
        logger.info("浏览器窗口最大化")
        driver.implicitly_wait(8)
        logger.info("隐式等待8秒")
        return driver

    def quit_browser(self):
        self.driver.quit()
        logger.info("关闭并停止浏览器服务")
