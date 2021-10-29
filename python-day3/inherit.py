class A:
    def __init__(self):
        print("calling A's ")
    def attr(self):
        print("A's Method")
class B(A):
    def __init__(self):
        print("B's COnst")
    def f(self):
        A.attr(self)
if __name__ == '__main__':
    b=B()
    b.f()