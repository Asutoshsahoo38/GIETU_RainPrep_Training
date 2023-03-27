class Employee:
    def __init__(self):
        self.employee_id = None
    def check_eligiblity(self):
        if(self.employee_id>=9000 and self.employee_id<=10000):
            print("The employee is eligible for special benefits")
        else:
            print("The employee is not eligible for special benefits")
emp1 = Employee()
emp1.employee_id = 10000
emp1.check_eligiblity()
emp2 = Employee()
emp2.employee_id = 2000
emp2.check_eligiblity()

#-------------------------------------------------------------
class Example:
    def __init__(self,num):
        self.num = num
    def set_num(self,num):
        self.num = num
    def get_num(self):
        return self.num
obj = Example(10)
print(obj.set_num())
obj.set_num(15)
print(get_num())

#-------------------------------------------------------------
class Shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material
s = Shoe(1000,'canvas')
print(s.price)
print(s.material)

#------------------------------------------------------------
class Shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material
s = Shoe(1000,'canvas')
print("the unique id of the onject is :", id(s))

#------------------------------------------------------------
class Mobile:
    def __init__(self):
        print(id(self))  ## Object is created but no reference variable is created
    def display(self):
        print("Display details")
    def purchase(self):
        self.display()
        print("Calculating price")
Mobile().purchase()        

#-----------------------------------------------------------
class Mobile:
    def __init__(self,price,brand):
        self.price = price
        self.brand = brand
        self.total_price = None 
    def purchase(self):
        if self.brand == "Apple":
            discount = 10
        else:
            discount = 5
        self.total_price = self.price - self.price * (discount/100)
        print("Total price of ",self.brand , "is ",self.total_price)
m1 = Mobile(100000,"Apple")
m1.purchase()        
Mobile(600000,'Nokia').purchase()
#-------------------------------------------------------------
class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age 
        self.wallet_balance = wallet_balance 
    def update(self,amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount
    def show_balance(self):
        print("Total balance is ", self.wallet_balance)
        
c1 = Customer(100,'Ashu',24,1000)
c1.update(500)
c1.show_balance()

#--------------------------------------------------------------
## Making private to wallet balance

class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age 
        self.__wallet_balance = wallet_balance ## Wallet balance is Private
    def update(self,amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount
    def show_balance(self):
        print("Total balance is ", self.__wallet_balance)
        
c1 = Customer(100,'Ashu',24,1000)
c1.update(500)
c1.show_balance()
print(#c1.__wallet_balance) ## Private wallet balance can't be access outside the class
#--------------------------------------------------------------------------
## To overcome from the problem of private
class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age 
        self.__wallet_balance = wallet_balance ## Wallet balance is Private
    def update(self,amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount
    def show_balance(self):
        print("Total balance is ", self.__wallet_balance)
    def value(self):
        return self.__wallet_balance
        
c1 = Customer(100,'Ashu',24,1000)
c1.update(500)
c1.show_balance()
print(c1.value) ## we can access to private file outside the class by returning
##the value through a fuction
#----------------------------------------------------------------------
class Dam:
    def __init__(self,name,length):
        
        self.name = name
        self.__length = length ##Private
    
    def get_length(self):
        return self.__length
        
c1 = Dam('ABC Dam',3.5)
print(c1.name)
print(c1.get_length())
#------------------------------------------------------------------------
class Table:
    def __init__(self):
        
        self.no_of_legs = 4
        self.__glass_top = None
        self.__wooden_top = None
dining_table = Table()
back_table = Table()
front_table = back_table
back_table = dining_table
print(dining_table,back_table,front_table)

