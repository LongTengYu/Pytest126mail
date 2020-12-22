'''所有allure装饰语句，可在一组用例中多次出现，当相同的allure装饰语句出现多次时，已离用例最近的allure装饰语句为准！！！'''
import os
import pytest
import allure

# 用pytestmark方法。在本测试用例中集中声明一些套件名称和套件父子关系
pytestmark = [pytest.mark.OrderWork,
              allure.parent_suite("创建基础数据"),  # parent_suite表示suite套件的父套件
              allure.suite("基础数据"),  # suite表示套件
              allure.sub_suite('工单基础数据')  # sub_suite表示suite的子套件
              ]

@allure.feature('模块1')  #声明模块名称
@allure.link(url='https://www.cnblogs.com/poloyy/p/12726946.html',name='访问连接')  #访问连接
@allure.issue(url='https://baike.baidu.com/item/bug/3353935?fr=aladdin',name='Bug连接')  #Bug连接
@allure.testcase(url='https://www.zhihu.com/question/51558124',name='用例连接') #用例连接
@allure.description('用例描述')  #声明描述
@allure.title('第一个测试类')
class TestA():
    @allure.story('模块1-用例a1') #声明模块名称下的子名称（一般用作用例名称）
    @allure.severity(allure.severity_level.CRITICAL) #定义优先级
    # @allure.step('测试步骤') #说明测试步骤
    @allure.description('用例a1描述') #再次声明描述。
    @allure.link(url='https://www.baidu.com', name='百度连接') #增加连接
    @allure.suite('这是套件') #声明套件名称
    @allure.title('第一个测试用例') #声明测试标题名称，多用于增加中文标

    @allure.story('模块1-用例a2')
    def test_a2(self):
        print('a2')

@allure.feature('模块2')
class TestB():
    @allure.story('模块2-用例b1')
    def test_b1(self):
        print('b1')

    @allure.story('模块2-用例b2')
    def test_b2(self):
        print('b2')


if __name__ == '__main__':
    # 运行Allure.py文件，-v表示显示每一个用例执行的结果 ，-s表示显示print内容
    # --alluredir表示用allure生成的测试数据
    pytest.main(['12、Allure.py','-v','-s'])

    # 创建Html报告,注意一下语法中间的空格。--clean表示覆盖上一个Html文件
    # 语句：allure generate '测试结果数据路径' -o 'Html文件的存放路径' --clean
    split = 'allure '+'generate '+'./AllureHtml '+'-o '+'./AllureHtml/Html '+'--clean'
    os.system(split)


    # 1、生成测试报告数据
    # pytest --alluredir =./AllureHtml
    #
    # 2、测试报告在线预览
    # allure serve  ./AllureHtml
    #
    # 3、测试报告本地静态数据生成
    # allure generate ./AllureHtml -o ./AllureHtml/Html

    # 4、查看Html报告
    # allure open -h 127.0.0.1 -p 8083 ./Report/Zip/Report/Html


    #参考文章：
    # 1、Allure测试报告使用心得：https://my.oschina.net/leichen/blog/4399950
    # 2、pytest+allure 使用的简单教程：https://www.cnblogs.com/liangdian/p/13688826.html
    # 3、pytest+allure之测试报告本地运行:https://www.jianshu.com/p/58c5bc570885