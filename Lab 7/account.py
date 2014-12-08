#Lab 7
#File 1 of 3
#Joe Guarni
#CISC106 - 7/22/13

#AssertEquals can be found in the main function.

from cisc106 import *

#Problem 1

class Account:

    """

    An account is database that holds financial information in an
    organized manner.

    first_name -- string
    last_name -- string
    balance -- integer
    interest -- integer

    """

    def __init__(self,first_name,last_name,balance,interest):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = balance
        self.__interest = interest

    """

    def Account_function(aAccount):
        return Account.first_name
               Account.last_name
               Account.balance
               Account.interest
               
    """
        
    def getFirstName(self):

        """
        Gets the private variable.

        """
        return self.__first_name
    def getLastName(self):

        """
        Gets the private variable.

        """
        return self.__last_name
    def getBalance(self):
        
        """
        Gets the private variable.

        """
        return self.__balance
    def getInterestRate(self):

        """
        Gets the private variable.

        """
        return self.__interest

    def deposit(self,amount):

        """
        Adds a given amount of money to the customers account.

        amount -- integer
        return -- boolean

        """
        self.__balance += amount
        return True
        
    def withdraw(self,amount):

        """

        Withdraws a given amount of money from a customers account.

        amount -- integer
        return -- boolean

        """
        
        if (self.__balance >= amount):
            self.__balance = self.__balance - amount
            return True
        else:
            return False
        
    def transfer(self,amount,origin,destination):
        
        """

        Transfers funds from one account to another account.

        amount -- integer
        origin -- Account Balance
        destination -- Account Balance

        """
        
        if (amount <= origin.__balance):
            origin.__balance = origin.__balance - amount
            destination.__balance = destination.__balance + amount
            print("The Destination balance is now $",destination.__balance)
            return True
        else:
            print("Insufficient Funds")
            return False
        
    def accrueInterest(self,time):

        """

        This function will tell a user their account balance after it
        has accrued interest for a given amount of months.

        time -- integer (amount of months)

        return -- Account balance

        """
        ainterest = float(self.__balance) * float(self.__interest) * float(time)
        
        self.__balance = self.__balance + float(ainterest)

        return self.__balance

    def __str__(self):

        """

        This function prints and returns all of the account holders information
        stored in the class Account.

        return -- string

        """
        
        return "The customers name is: " + self.__first_name + ' ' + self.__last_name \
               + "\nThe balance is: $" + str(self.__balance) + "\nThe interest rate is: " \
               + str(self.__interest) + '%'

#Problem 2
    
def getAccountInformation(aList):

    """

    This function will print the details after the user has typed in both the
    first and last name verifying it is their account.

    aList -- List of Accounts

    """
    
    first_name = input("What is you first name? ").lower()
    last_name = input("What is your last name? ").lower()

    for ele in aList:
        
       if (first_name == ele.getFirstName()) and (last_name == ele.getLastName()):
           print(ele.__str__())

def totalBalance(aList,sumall):

    """

    This function will recursivly sum all of the balances in all of the
    accounts.

    return -- sum of all accounts.

    """
    
    
    if (len(aList) == 0):
        return sumall
    else:
        sumall = sumall + aList[0].getBalance() + totalBalance(aList[1:],sumall)
        return sumall
    
def executeTransfer(aList):

    """

    This function will get the required information in order to process
    a transfer of money from one account to another. It will ask the user
    for their origin name, amount of money to transfer, and destination name.

    aList -- List of Accounts

    """
    
    print("This function will be used to transfer money.")

    origin_first = input("What is the first name on the origin account? ").lower()
    origin_last = input("What is the last name on the origin account? ").lower()
    amount = int(input("How much would you like transferred? "))
    dest_first = input("What is the first name on the destination account? ").lower()
    dest_last = input("What is the last name on the destination account? ").lower()

    for ele in aList:
        
       if (origin_first == ele.getFirstName()) and (origin_last == ele.getLastName()):
           origin_account = ele
       if (dest_first == ele.getFirstName()) and (dest_last == ele.getLastName()):
           destination_account = ele
           origin_account.transfer(amount,origin_account,destination_account)

def executeAccrue(aList):

    """

    This function will recieve the required information in order to tell you
    the accured interest on an account. It will ask for a first and last name
    and how many months to accrue interest for.

    aList -- list of Accounts

    """
    
    accrue_first = input("What is the first name on the account? ").lower()
    accrue_last = input("What is the last name on the account? ").lower()

    for ele in aList:
        if (accrue_first == ele.getFirstName()) and (accrue_last == ele.getLastName()):
            time_period = input("Accure interest for how many months? ")
            print("The account balance plus accrued interest is: $",ele.accrueInterest(time_period))



            
def main():

    """

    This function will be used to set accounts and also set up a menu for the user.
    This menu will ask them what type of changes they want to make to thier account
    or what information they want to receive. It will make the necessary calls to the
    functions needed to complete these tasks.

    """
    
    account1 = Account("joe","guarni",50000,0.2)
    account2 = Account("john","smith",1500,0.1)
    account3 = Account("travis","barker",500000,0.3)
    account4 = Account("bobby","man",4000,0.1)
    account5 = Account("dave","daman",100000000,0.2)
    account6 = Account("steve","adams",500,0.6)


    aList = [account1,account2,account3,account4,account5,account6]

    assertEqual(totalBalance(aList,0),100556000)

        
    assertEqual(Account.withdraw(account1,0),True)
    assertEqual(Account.withdraw(account2,0),True)
    assertEqual(Account.withdraw(account3,0),True)

    assertEqual(Account.getBalance(account1),50000)
    assertEqual(Account.getBalance(account2),1500)
    assertEqual(Account.getBalance(account3),500000)

    assertEqual(Account.transfer(0,0,account1,account2),True)
    assertEqual(Account.transfer(0,100000000,account3,account4),False)
    assertEqual(Account.transfer(0,0,account5,account6),True)
    
    assertEqual(Account.deposit(account1,0),True)
    assertEqual(Account.deposit(account2,0),True)
    assertEqual(Account.deposit(account3,0),True)
 
    assertEqual(Account.getFirstName(account1),"joe")
    assertEqual(Account.getFirstName(account2),"john")
    assertEqual(Account.getFirstName(account3),"travis")

    assertEqual(Account.getLastName(account1),"guarni")
    assertEqual(Account.getLastName(account2),"smith")
    assertEqual(Account.getLastName(account3),"barker")

    assertEqual(Account.getInterestRate(account1),0.2)
    assertEqual(Account.getInterestRate(account2),0.1)
    assertEqual(Account.getInterestRate(account3),0.3)

    print('Testing Over\n')
    print('--------------------------------------------------')
    

    print("Welcome to Python's Banking Terminal!\n")
    print("Please choose from the following menu options.\n")

    print("1. Get an account balance\n"
         
          "2. Get the total balance of all accounts\n"
          "3. Accrue interest in an account\n"
          "4. Realize a transfer\n"
          "5. Exit")

    user_input = int(input("->>>>>>>>>: "))

    if (user_input == 1):
        getAccountInformation(aList)
    if (user_input == 2):
        print(totalBalance(aList,sumall=0))
    if (user_input == 3):
        executeAccrue(aList)
    if (user_input == 4):
        executeTransfer(aList)
    if (user_input == 5):
        return
        
main()
