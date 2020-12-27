class A():
    def aa(self):
        print('aa')
class B():
    def bb(self):
        print('bb')

class C(A,B):
    def cc(self):
        print('cc')

class D(C):
    def dd(self):
        print('dd')

if __name__=='__main__':
    x=D()
    x.dd()
