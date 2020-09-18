class A1(object):
    def f(self):
        print('A1')


class A2(object):
    def f(self):
        print('A2')


class B0(object):
    def f(self):
        super().f()
        print('B')

class C1(B0, A1):
    pass

class C2(B0, A2):
    pass

x = C2()
y = B0()

x.f()
y.f()
