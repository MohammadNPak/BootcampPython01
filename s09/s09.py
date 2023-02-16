

# class Date:
#     origin_day_of_week = 4

#     def __init__(self,year,month,day) -> None:
#         self.year = year
#         self.month = month
#         self.day = day
    
#     def __str__(self) -> str:
#         return f"Date(year={self.year},month={self.month},day={self.day})"

#     def get_days(self):
#         return self.day+ self.month*30 + self.year*360
    
#     def day_of_week(self):
#         pass

#     def __add__(self,obj):
#         if isinstance(obj,Date):
#             day = self.get_days()+obj.get_days()
#             year = day//360
#             day = day%360
#             month = day//30
#             day = day%30
#             return Date(year,month,day)
    
#     def __sub__(self,other):
#         pass
            

# date1 = Date(1370,1,3)
# date2 = Date(1440,3,12)
# date3 = Date(10,3,1)

# result = date1+date3
# print(result)


# from datetime import date

# d1 = date(1991,3,23)
# d2 = date(2003,5,10)

# delta_date = d2-d1
# print(type(delta_date))
# print(dir(d1))


# class Card:

#     _hokm = 0
#     _active_suit = 0
#     _suit2num = {'♥':0,'♦':1,'♣':2,'♠':3}
#     _num2suit = {0:'♥',1:'♦',2:'♣',3:'♠'}

#     def __init__(self,number,suit:int):
#         self.number = number
#         self.suit =suit
    
#     @classmethod
#     def set_hokm(cls,hokm):
#         if 0<=hokm<4:
#             cls._hokm = hokm
#         else:
#             raise Exception("hokm must be in 0<= hokm < 4 ")
    
#     @classmethod
#     def set_active_suit(cls,suit):
#         if 0<=suit<4:
#             cls._active_suit = suit
#         else:
#             raise Exception("hokm must be in 0<= hokm < 4 ")

#     @classmethod
#     def number_to_suit(cls,number):
#         return cls._num2suit[number]
    
#     @classmethod
#     def suit_to_number(cls,suit):
#         return cls._suit2num[suit]

#     def __gt__(self,other):
#         if self.suit == Card._hokm and other.suit != Card._hokm:
#             return True
#         elif self.suit == Card._hokm and other.suit == Card._hokm:
#             return True if self.number > other.number else False
#             # return self.number > other.number
#         elif self.suit != Card._hokm and other.suit == Card._hokm:
#             return False
#         elif self.suit != Card._hokm and other.suit != Card._hokm:
#             if self.suit == Card._active_suit and other.suit != Card._active_suit:
#                 return True
#             elif  self.suit == Card._active_suit and other.suit == Card._active_suit:
#                 return self.number > other.number
#             elif  self.suit != Card._active_suit and other.suit == Card._active_suit:
#                 return False
#             elif  self.suit != Card._active_suit and other.suit != Card._active_suit:
#                 return self.suit > other.suit
        

#     def __lt__(self,other):
#         pass
    

# print('❤️')
# a = Card(2,0)
# b = Card(5,2)
# a.set_hokm(0)
# a>b
# print(Card.suit_to_number('♥'))


# def sample_decorator(f):
#     def wraper():
#         f()
#         print("salam")
#     return wraper

# @sample_decorator
# def sample_def():
#     print('hello')

# sample_def = sample_decorator(sample_def)


class Father:
    def __init__(self,name) -> None:
        self.name = name
        self.gender = "male"

class Mother:
    def __init__(self,name) -> None:
        self.name = name
        self.gender = "female"

class Student(Father,Mother):
    def __init__(self, n,id) -> None:
        self.student_id = id
        super(Mother).__init__(n)

p1 = Father("mohamad")
p2 = Mother("mahdieh")
s = Student("ali",123)

print(p1.__dict__)
print(p2.__dict__)
print(s.__dict__)