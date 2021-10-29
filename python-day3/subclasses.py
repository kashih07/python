class EmpA:
    def __init__(self,name,age,sal):
        print("calling A's ")
        self.name=name
        self.age=age
        self.sal=sal
    def attr(self):
        print("Name is : "+str(self.name))
        print("AGE : "+str(self.age))
        print("Sal : "+str(self.sal))
class EmpB(EmpA):
    def __init__(self,name,age,sal,place):
        print("B's COnst")
        super().__init__(name,age,sal)
        self.place=place
    def attr(self):
        #super().attr()
        print("Place : "+str(self.place))
if __name__ == '__main__':

    b=EmpB("kashi",22,27000,"sagar")
    b.attr()