#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/20 11:44
# @Author  : owen
# @File    : base_page.py

import time
from selenium.common.exceptions import NoSuchElementException
import os.path
from framework.logger import Logger
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 创建一个logger实例
logger = Logger(logger="BasePage").getLog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # 退出浏览器操作
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("在当前页面点击前进按钮")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("在当前页面点击后退按钮")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("等待 %d 秒" % seconds)

    # 关闭当前窗口操作
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭当前窗口")
        except NameError as e:
            logger.error("关闭当前窗口失败 %s" % e)

    # 保存图片
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\screenshots下
        :return:
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("截图并保存到文件夹：/screenshots下")
        except NameError as e:
            logger.error("截图失败！%s" % e)
            self.get_windows_img()

    # 定位元素方法
    def find_element(self, selector):
            """
            这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
            submit_btn = "id=>su"
            login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
            如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
            :param selector:
            :return: element
            """
            element = ''
            if '=>' not in selector:
                return self.driver.find_element_by_id(selector)
            selector_by = selector.split('=>')[0]
            selector_value = selector.split('=>')[1]

            if selector_by == "i" or selector_by == 'id':
                try:
                    element = self.driver.find_element_by_id(selector_value)
                    logger.info("Had find the element \' %s \' successful "
                                "by %s via value: %s " % (element.text, selector_by, selector_value))
                except NoSuchElementException as e:
                    logger.error("NoSuchElementException: %s" % e)
                    self.get_windows_img()  # 报错截图
            elif selector_by == "n" or selector_by == 'name':
                element = self.driver.find_element_by_name(selector_value)
            elif selector_by == "c" or selector_by == 'class_name':
                element = self.driver.find_element_by_class_name(selector_value)
            elif selector_by == "l" or selector_by == 'link_text':
                element = self.driver.find_element_by_link_text(selector_value)
            elif selector_by == "p" or selector_by == 'partial_link_text':
                element = self.driver.find_element_by_partial_link_text(selector_value)
            elif selector_by == "t" or selector_by == 'tag_name':
                element = self.driver.find_element_by_tag_name(selector_value)
            elif selector_by == "x" or selector_by == 'xpath':
                try:
                    element = self.driver.find_element_by_xpath(selector_value)
                    logger.info("Had find the element \' %s \' successful "
                                "by %s via value: %s " % (element.text, selector_by, selector_value))
                except NoSuchElementException as e:
                    logger.error("NoSuchElementException: %s" % e)
                    self.get_windows_img()
            elif selector_by == "s" or selector_by == 'selector_selector':
                element = self.driver.find_element_by_css_selector(selector_value)
            else:
                raise NameError("请输入有效目标元素")

            return element

    # 输入
    def input(self, selector, text):

            # type("id=>kw", "selenium")
            el = self.find_element(selector)
            el.clear()
            try:
                el.send_keys(text)
                logger.info("在已有输入框中输入 \' %s \'" % text)
            except NameError as e:
                logger.error("在文本框中输入失败 %s" % e)
                self.get_windows_img()

    # 清楚文本框
    def clear(self, selector):
            el = self.find_element(selector)
            try:
                el.clear()
                logger.info("清除文本框内容")
            except NameError as e:
                logger.error("清除文本框内容失败 %s" % e)
                self.get_windows_img()

    # 点击元素
    def click(self, selector):
            el = self.find_element(selector)
            try:
                el.click()
                logger.info("点击 \' %s \' 元素成功." % el.text)
            except NameError as e:
                logger.error("点击 \' %s \' 元素失败" % e)

    # 获取网页标题
    def get_page_title(self):
            logger.info("当前页面的标题是 %s" % self.driver.title)
            return self.driver.title

    @staticmethod
    def sleep(seconds):
            time.sleep(seconds)
            logger.info("等待 %d 秒" % seconds)
