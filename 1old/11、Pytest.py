import pytest  # 引用pytest
import yaml
import allure


def add(n):
    return n + 1


class TestC():  # 声明测试类
    print('TestC')

    def dd(self):
        print('dd')

    def test_add(self):  # 声明测试方法
        assert add(3) == 4
        print('test')


@pytest.fixture()  # 修饰符，用于将修饰符下方第一个方法变成测试用例的前置操作
def first():
    print('前置操作')
    return 'Yu'


def test_sub(first):  # 引用fixture修饰的方法作为参数，参数名与方法名需一致
    print(f'a unsername={first}')  # 打印返回值


@pytest.mark.parametrize("a,b,x,y", [[10, 20, 30, 40], [50, 60, 70, 80]])  # 参数化用例
def test_para(a, b, x, y):
    c = a + b + x + y
    print(c)


# @pytest.mark.parametrize("a,b", yaml.safe_load(open("./data.yaml")))  # 调用yaml的参数化用例
# def test_para2(a, b):
#     c = a + b
#     print(c)

# y=yaml.safe_load(open("./data.yaml"))
# @pytest.mark.parametrize("a", y)  # yaml中字典类型数据的尝试，以调试模式运行更易读懂yaml数据的特性
# def test_para3(a):
#     if "test" in a:
#         print(a)
#         print(yaml.safe_load(open("./data.yaml")))
#     else:
#         print("未匹配成功")
#         print(a)
#         print(yaml.safe_load(open("./data.yaml")))


# if __name__ == '__main__':
#     pytest.main(['11、Pytest.py::', '-v', '-s'])  # 运行pytest文件，-v表示显示每一个用例执行的结果 ，-s表示显示print内容

if __name__ == '__main__':
    pytest.main(['11、Pytest.py::TestC::test_add', '-v', '-s'])  #调用单个用例

'''
pytest详解：https://blog.csdn.net/lovedingd/article/details/98952868
fixture详细使用：https://www.cnblogs.com/huizaia/p/10331469.html
'''
