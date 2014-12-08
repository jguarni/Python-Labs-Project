# CISC106
# Joe Guarni
# Lab 3 6/17/2013

from cisc106 import *


#Problem 1

"""

Given the call to the function j: j(3,2,4)

1) 3
2) 4
3) 2
4) 4

Given the call to the function k: k(3,4,2)

5) 4
6) 3
7) 3
8) 3

Given the call to the function l: l(5,7,9)

09) 4
10) 14
11) 9
12) 8

"""

#Problem 2

def first_if_func(x):
    
    """
    This function will determine what equation to use depending on the input
    and return the value of that equation.

    x -- number

    return -- number

    """
    
    if (x < 7):
        return -1 * x**3
    else:
        return x**2
    
assertEqual(first_if_func(1), -1)
assertEqual(first_if_func(8), 64)
assertEqual(first_if_func(9), 81)

#Problem 3

def second_if_func(x,y):

    """
    This function will determine which equation to use depending on the value
    of the input, and return the value of that equation.

    x -- number
    y -- number

    return -- number
    
    """
    
    if (y > 0):
        return (y**2)/x
    elif (y < 0):
        return ((x*-2)**3)/y
    else:
        return x

assertEqual(second_if_func(1,2),4)
assertEqual(second_if_func(1,-2),4)
assertEqual(second_if_func(1,0),1)

#Problem 4

def calc_grade(x,y,z,q):
    
    """
    This function will determine which equation to use depending on if the
    student is a graduate(0) or an undergraduate(1) and use their specific
    grading equation accordingly to produce a grade.

    x -- number
    y -- number
    z -- number
    q -- number

    return -- number
    
    """
    
    if (q == 1):
        return ugrade(x,y,z)
    elif (q == 0):
        return ggrade(x,y,z)
    else:
        return -1

def ugrade(x,y,z):

    """
    This function will take the the grade values (x,y,z) and return the
    calculated grade when it passes through the equation.

    x -- number
    y -- number
    z -- number

    return -- number
    
    """
    return 1.2 * ((x+y+z)/320)

def ggrade(x,y,z):

    """
    This function will take the the grade values (x,y,z) and return the
    calculated grade when it passes through the equation.

    x -- number
    y -- number
    z -- number

    return -- number
    
    """
    return 0.9 * ((x+y+z)/340)

assertEqual(calc_grade(5,6,9,1), 0.075)
assertEqual(calc_grade(102,102,102,0), 0.81)
assertEqual(calc_grade(15,15,10,1), 0.15)
assertEqual(calc_grade(15,15,10,10), -1)

#Problem 5

def pieces_produced(hour, workers):
    
    """
    This function will return how many pieces can be produced
    depending on the hour of the day and the number of workers
    present at that time.

    hour -- number
    workers -- number

    return -- number

    """
    
    if (hour >= 6) and (hour < 10):
        return 30 * (hour - 6) * workers
    elif (hour >= 10) and (hour < 14):
        return (30 * 4 * workers) + (40 * (hour - 10) * workers)
    elif (hour >= 14) and (hour < 18):
        return (30 * 4 * workers) + (40 * (hour - 10) * workers) + (35 * (hour - 14) * workers)
    
assertEqual(pieces_produced(8,10), 600)
assertEqual(pieces_produced(12,15), 3000)
assertEqual(pieces_produced(16,10), 4300)

#Problem 6

def bill_amount(transfer, base):
    
    """
    This function will determine the users bill amount based on the
    amount of data transfered and the market condition base rate.

    tranfer -- number
    base -- number

    return -- number

    """
    
    if (transfer <= 100):
        return transfer * base
    elif (transfer <= 500):
        return transfer * (base * 1.33 + 0.05)
    elif (transfer <= 1500):
        return transfer * (base * 1.44 + 0.08)
    elif (transfer > 1500):
        return transfer * (base * 2)

assertEqual(bill_amount(50,0.25), 12.5)
assertEqual(bill_amount(300,0.25), 114.75)  
assertEqual(bill_amount(600,0.25), 264)
assertEqual(bill_amount(1600,0.25), 800)

#Problem 7

def mortgage_approval(lamount, ysalary, ccash, ncash, cscore, lname):
    
    """
    This function will take variables that determine weather or not
    a person is eligible for the loan amount they are asking for. It
    will either tell you that you are approved (True) or that you were not
    approved (False).

    lamount -- number
    ysalary -- number
    ccash -- number
    ncash -- number
    cscore -- number
    lname -- string

    return -- boolean

    """
    
    credit_ratio = (cscore - 550)/250
    adjusted_balance = lamount - ccash
    expected_income = 10 * (ysalary + ncash)
    risk_metric = ((expected_income * credit_ratio) - adjusted_balance) / adjusted_balance

    if (ccash < (.10 * lamount)):
        return False
    else:
        if (cscore < 600):
            return False
        else:
            if (cscore > 600) and (cscore < 700) and (ccash < .20 * lamount):
                return False
            else:
                if (ysalary < .10 * (lamount - ccash)):
                    return False
                else:
                    if (lname == 'Smith') and (ncash < 1000000):
                        return False
                    else:
                         if (ccash >= lamount):
                            return True
                         else:
                             if (ccash < lamount) and (risk_metric < 2):
                                 return False
                             else:
                                 if (ccash < lamount) and (risk_metric >= 2):
                                     return True
                         

# bad cash in accounts
print("\n---bad cash in accounts")
assertEqual(mortgage_approval(200000, 500000, 0, 1000000, 800, "Fox"), False)
 
# bad credit score
print("\n---bad credit score")
assertEqual(mortgage_approval(200000, 500000, 500000, 1000000, 500, "Fox"), False)
 
# not enough cash in account for credit score between 600/700
print("\n---not enough cash in account for credit score between 600/700")
assertEqual(mortgage_approval(200000, 500000, 20000, 1000000, 650, "Fox"), False)
 
# salary not enough
print("\n---salary not enough")
assertEqual(mortgage_approval(200000, 5000, 50000, 1000000, 800, "Fox"), False)
 
# Smith does not have enough assets
print("\n---Smith does not have enough assets")
assertEqual(mortgage_approval(200000, 500000, 50000, 500000, 800, "Smith"), False)
 
# passes all previous tests and has cash > amount
print("\n---passes all previous tests and has cash > amount")
assertEqual(mortgage_approval(200000, 20000, 200001, 0, 750, "Fox"), True)
 
# passes all previous tests but has risk metric < 2 (about 1.8)
print("\n---passes all previous tests but has risk metric < 2 (about 1.8)")
assertEqual(mortgage_approval(200000, 20000, 20000, 0, 750, "Fox"), False)
 
# passes all previous tests and has risk metric > 2 (about 4.2)
print("\n---passes all previous tests and has risk metric > 2 (about 4.2)")
assertEqual(mortgage_approval(200000, 75000, 20000, 0, 750, "Fox"), True)
    
