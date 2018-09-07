#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 16:51
# @Author  : owen
# @File    : TestRunner.py

import HTMLTestRunner
import os
import time
import unittest
from testsuits.baidu_search import BaiduSearch
from testsuits.test_get_page_title import GetPageTitle
from testsuits.test_nba_news_view import SportNewsHomePage

#设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'

#获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

#设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = file(HtmlFile,"wb")


#方法三：直接加载项目路径下的所有测试包及测试类
suite = unittest.TestLoader().discover("testsuits") #包名


#方法二：直接加载测试类
#suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))
#suite(unittest.makeSuite(GetPageTitle))

#方法一：加载测试函数（方法）
# suite.addTest(BaiduSearch('test_baidu_search'))
# suite.addTest(BaiduSearch('test_search2'))
# suite.addTest(GetPageTitle('test_get_title'))
# suite.addTest(SportNewsHomePage('test_view_nba_views'))

if __name__ == '__main__':

    #初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"项目测试报告", description=u"用例测试情况")
    #执行用例
    #runner = unittest.TextTestRunner()
    runner.run(suite)
