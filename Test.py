class BasePage():
    def testa(self, a1):
        self.aa = a1
        print(self.aa)

    def testb(self):
        self.bb = '2'
        print(self.bb)

    def testc(self):
        self.c='3'
        print(self.c)

class LoginPage(BasePage):
    def log(self):
        self.testc()

class setup(BasePage):
    def setup_class(self):
       # 用对象调用BasePage类里的testa函数，因test_user_login调用setup_class时是当成一个方法来调用的，
       # 所以当用对象调用testa函数时，必须传入一个对象（self）
        self.testa('1')
        self.testb()

class testlogin(setup,LoginPage):
    def test_user_login(self):
        setup.setup_class(self)  #因没有对setup进行实例化，就直接调用setup的setup_class方法

class testclass():
    @classmethod
    def tc(cls):
        print(type(cls),cls)

testclass.tc()
run=testlogin()
run.test_user_login()
run.log()

#参考文档：https://www.cnblogs.com/kaibindirver/p/10718793.html



