class A():
    def aa(self,a):
        print('aa:',a)
        self.dd=a

class B(A):
    def bb(self):
        self.aa(1)

class C(B):
    def cc(self):
        self.bb(self,1)


