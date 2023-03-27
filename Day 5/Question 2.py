## A student is taking admission with some condition they takes admission 
class Student:
    def __init__(self,id,marks,Age):
        self.__id = id
        self.__marks = marks
        self.__Age = Age
        self.__course_id = None
    def Validate_marks(self):
        if (self.__marks >=0) and (self.__marks <= 100):
            return True
        else:
            return False
    def Validate_age(self):
        if (self.__Age > 20):
            return True
        else:
            return False
    def checkQualification(self):
        if self.Validate_age() and self.Validate_marks():
            if (self.__marks>=65):
                return self.course_price()
        else:
            print('Not Qualified')
        
        
    def course_price(self):
        d = {1001:3500,1002:45000,1003:1200}
        discount = 0
        if(self.__marks>=85):
            discount = 0.25
        return d[self.__id] - discount * d[self.__id] 
A = Student(1001,80,21) 
print(A.checkQualification())
            
