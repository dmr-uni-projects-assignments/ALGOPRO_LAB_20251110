class Account:
    def __init__(self, balance):
        self.__balance = balance
        pass
    
    def getBalance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw (self, amount):
        if (self.__balance - amount < 0):
            print("not enough balance")
        else:
            self.__balance -= amount

class Customer:
    def __init__(self, fn, ln):
        self.__firstName = fn
        self.__lastName = ln
        self.__account = Account(0)
        pass
    
    def getFirstName(self):
        return self.__firstName
    
    def getLastName(self):
        return self.__lastName
    
    def getAccount(self):
        return self.__account
    
    def setAccount(self, acc):
        self.__account = acc
        
class Bank:
    def __init__(self, bn):
        self.__bankName = bn
        self.__customers = []
        self.__numberOfCustomers = 0
        pass
    
    def addCustomer(self, f, l):
        cust = Customer(f, l)
        self.__customers.append(cust)
        self.__numberOfCustomers += 1
        
    def getNumberOfCustomers(self):
        return self.__numberOfCustomers
    
    def getCustomer(self, index):
        if index >= len(self.__customers):
            print("index out of bounds, try again")
            return Customer("Not Found", "Error")
        
        return self.__customers[index]
    
