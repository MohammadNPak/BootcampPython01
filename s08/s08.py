# oop

# camel case
# firstName

# snake case
# first_name

# pascal case
# FirstName

# lazy case
# firstname

# macro
# FIRST_NAME

# kebbab case
# first-name-of-studen

# pep8
# type hint

# class Student:
#     country = 'iran'

#     def __init__(self,name,id) -> None:
#         self.name1 = name
#         self.id1 = id
        
        
#     def __repr__(self) -> str:
#         return f"student object"

#     def __str__(self) -> str:
#         return f"str method from student"
    
#     def say_hello(self):
#         print(self)
#         self.phone = "232323"
#         return f"hello {self.name1}!"
       
#     def say_goodbye(self):
#         return f"good bye!"

# a = Student('mohammad','1234')
# b = Student('ali','321')

# print(a.say_hello())
# print(b.say_hello())
# print(hex(id(a)))
# print(hex(id(b)))

# c = str(a)



class Person:
    
    def __init__(self,name,phone,address) -> None:
        self.name = name
        self.phone = phone
        self.address = address

    def info(self):
        return f"this is {self.name},phone:{self.phone},address:{self.address}"
    


class PhoneBook:
    def __init__(self,phonebook_name) -> None:
        self.phonebook_name = phonebook_name
        self.contacts = []

    def add_person(self,p):
        if not isinstance(p,Person):
            raise Exception('input type must be Pesron')
        self.contacts.append(p)
    
    def remove_contacts(self,name):
        # self.contacts.remove(list(filter(lambda x:x.name==name,self.contacts)[0]))
        for i,p in enumerate(self.contacts):
            if p.name == name:
                self.contacts.pop(i)
                break
    
    def show_contacts(self):
        for i,p in enumerate(self.contacts):
            print(f"#{i} {p.info()}") 

    def call_person(self,name):
        print(f"calling {next(filter(lambda x:x.name==name,self.contacts)).phone}")
    

phone_book = PhoneBook('first')
p1 = Person('mohammad','09123456789','dadsfafsad')
p2 = Person('ali','09123456789','fdsgdfgfg')dfdfbfvgfgfgfgfgfgf
phone_book.add_person(p1)
phone_book.add_person(p2)
phone_book.show_contacts()
phone_book.call_person('mohammad')

