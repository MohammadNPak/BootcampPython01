

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


class Card:

    _hokm = 0
    _suit2num = {'♥':0,'♦':1,'♣':2,'♠':3}
    _num2suit = {0:'♥',1:'♦',2:'♣',3:'♠'}

    def __init__(self,number,suit):
        self.number = number
        self.suit =suit
    
    @classmethod
    def number_to_suit(cls,number):
        return cls._num2suit[number]
    
    @classmethod
    def suit_to_number(cls,suit):
        return cls._suit2num[suit]

    def __gt__(self,other):
        pass

    def __lt__(self,other):
        pass
    

print('❤️')