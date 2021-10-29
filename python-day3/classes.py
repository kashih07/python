class ops:
    ecount=0
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
        ops.ecount+=1
    def printnamesal(self):
        print(getattr(self,"name"))
        print(getattr(self,"sal"))
    def f(self):
        print(self.ecount)
if __name__ == '__main__':
    x=ops("kashi",1000)
    x.printnamesal()
    y=ops("harshith",1000)
    setattr(y,"sal",y.sal*1.2)
    y.printnamesal()
    print(ops.__name__)
    print(ops.__base__)
    print(ops.__dict__)
    print(ops.__doc__)
    print(ops.__module__)