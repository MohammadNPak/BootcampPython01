class Father:
    def __init__(self,name) -> None:
        self.name = name
        self.gender = "male"
        self.__money = 0

    @property
    def money(self):
        return self.__money
    
    
    @money.setter
    def money(self,a):
        if a>0:
            self.__money=a
        
    
    def __say_hello(self):
        print(f"hello i'm {self.name} and i'm father")

class Mother:
    def __init__(self,name) -> None:
        self.name = name
        self.gender = "female"
        self.__say_hello()

    def __say_hello(self):
        print(f"hello i'm {self.name} and i'm mother")

class Student(Father,Mother):
    def __init__(self, n,id) -> None:
        self.student_id = id
        super().__init__(n)
        # Mother.__init__(self,n)
    
    def _say_hello(self):
        print(f"hello i'm {self.name} and i'm a { 'boy' if self.gender=='male' else 'girl'}")

f = Father("mohamad")
m = Mother("mahdieh")
s = Student("ali",123)

# f.add_money(10)
# f.spend_money(100)

print(f.money)
f.money=-2000
print(f.money)
f.money=10
print(f.money)
f.money = f.money+2