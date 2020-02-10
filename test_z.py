"""自己定义测试用例的前置和后置 fixture"""
import allure
import pytest
@allure.step("步骤1")
def test_0(login):
    print("只登陆")
@allure.step("步骤2")
def test_1(login):
    #先登录，再去执行xxx
    print("xxxx")
@allure.step("步骤3")
@allure.testcase("http://101.132.144.58:8080/zentao/testcase-view-1-1.html")
def test_2(login,open_a):
    #先登录，打开a页面，再去执行yy
    print("yyy")
