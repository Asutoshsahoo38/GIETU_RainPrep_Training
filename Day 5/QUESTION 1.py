## FIND THE PREMIUM AMOUNT USING SET AND GET IN WHICH 2 WHEELER PREMIUM OF 2%
## AND 4 WHEELER OF 6%

class Car:
    def __init__(self,vechile_id,cost,vechile_type):
        self.__vechile_id = vechile_id
        self.__cost = cost
        self.__vechile_type = vechile_type
        self.__premium = None
    def set_vechile_id(self,vechile_id):
        self.__vechile_id = vechile_id
    def get_vechile_id(self):
        return self.__vechile_id 
    def set_cost(self,cost):
        self.__cost = cost
    def get_cost(self):
        return self.__cost
    def set_vechile_type(self,vechile_type):
        self.__vechile_type = vechile_type
    def get_vechile_type(self):
        return self.__vechile_type
    def detail(self):
    
        if (self.__vechile_type == 2):
            self.__premium = 2
        elif(self.__vechile_type == 4):
            self.__premium = 6
        
        self.calculate(self.__premium)
    def calculate(self,premium):
        self.__cost = self.__cost + (premium/100)*self.__cost
        self.set_cost(self.__cost)    
A = Car(101,100000,2)
A.set_vechile_type(4)
A.detail()

print(A.get_cost())

## FIND THE PREMIUM WITHOUT USING SET AND GET
class Car:
    def __init__(self,vechile_id,cost,vechile_type):
        self.__vechile_id = vechile_id
        self.__cost = cost
        self.__vechile_type = vechile_type
        self.__premium = None
    def calculate(self,premium,amount):
        amount = amount + (premium/100)*amount
        print(amount)
        
    def detail(self):
    
        if (self.__vechile_type == 2):
            self.__premium = 2
        elif(self.__vechile_type == 4):
            self.__premium = 6
        
        self.calculate(self.__premium,self.__cost)
            
A = Car(101,100000,2)
A.detail()

            
