# Joe Guarni
# Lab 6 - 7/15/2013
# CISC106

from cisc106 import *

#Problem 1

#Part A

def bubblesort(ilist):
    
    """

    This function will sort a list using the non-recursive
    bubblesort method.

    ilist -- unsorted list

    return -- sorted list

    """
   

    for ele in range(len(ilist)-1,0,-1):
        for ele2 in range(ele):
            if ilist[ele2] > ilist[ele2+1]:
                variable = ilist[ele2]
                ilist[ele2] = ilist[ele2+1]
                ilist[ele2+1] = variable
    return ilist

assertEqual(bubblesort([96,67,64,37,105,78,102,55,54]),[37, 54, 55, 64, 67, 78, 96, 102, 105])
assertEqual(bubblesort([9,5,7,8,3,5,6,1,9,5,6,2]),[1, 2, 3, 5, 5, 5, 6, 6, 7, 8, 9, 9])
assertEqual(bubblesort([10,35,20,15,13,80,60,53,42,52]),[10, 13, 15, 20, 35, 42, 52, 53, 60, 80])

#Part B

def bubble_sort_rec(ilist):
    
    """

    This fucntion will check to see if the list is sorted.

    ilist -- unsorted list of integers

    return -- sorted list of integers

    """
    
    if ilist==sorted(ilist):
        return ilist
    else:
        ilist=sort_recursion(ilist)
        return bubble_sort_rec(ilist)

def sort_recursion(ilist):
    
    """

    This function will preform the bubblesort sorting algorithm
    recursivley until the list is sorted.

    ilist -- unsorted list of integers

    return -- sorted list of integers
    

    """
    if len(ilist)==1:
        return ilist
    else:
        if ilist[0]>ilist[1]:
            ilist[0],ilist[1]=ilist[1],ilist[0]
    return [ilist[0]]+sort_recursion(ilist[1:])

assertEqual(bubble_sort_rec([10,35,20,15,13,80,60,53,42,52]),[10, 13, 15, 20, 35, 42, 52, 53, 60, 80])
assertEqual(bubble_sort_rec([9,5,7,8,3,5,6,1,9,5,6,2]),[1, 2, 3, 5, 5, 5, 6, 6, 7, 8, 9, 9])
assertEqual(bubble_sort_rec([10,35,20,15,13,80,60,53,42,52]),[10, 13, 15, 20, 35, 42, 52, 53, 60, 80])
    
#Problem 2

def quicksort(ilist):

    """

    This function will preform the quicksort sorting algorithm
    using recursion to sort the list.

    ilist -- unsorted list of integers

    return -- sorted list of integers

    """

    if (len(ilist) <= 1):
        return ilist
    
    pivot = ilist.pop()

    l_list = []
    r_list = []
    
    for ele in ilist:
        if ele <= pivot:
            l_list.append(ele)
        else:
            r_list.append(ele)
        
    slist = []

    if len(l_list) > 0:
        slist.extend(quicksort(l_list))

    slist.append(pivot)

    if len(r_list) > 0:
        slist.extend(quicksort(r_list))

    return slist

assertEqual(quicksort([96,67,64,37,105,78,102,55,54]),[37, 54, 55, 64, 67, 78, 96, 102, 105])
assertEqual(quicksort([9,5,7,8,3,5,6,1,9,5,6,2]),[1, 2, 3, 5, 5, 5, 6, 6, 7, 8, 9, 9])
assertEqual(quicksort([10,35,20,15,13,80,60,53,42,52]),[10, 13, 15, 20, 35, 42, 52, 53, 60, 80])

#Problem 3

#Part A

def insertionsort(ilist):

    """

    This function will preform the insertionsort sorting
    algorithm through a non-recursive function.

    ilist -- unsorted list of integers

    return -- sorted list of integers

    """

    for i in range(1,len(ilist)):
        variable = ilist[i]
        insert = i
        while insert > 0 and variable < ilist[insert - 1]:
            ilist[insert] = ilist[insert - 1]
            insert -= 1
        ilist[insert] = variable
    return ilist

assertEqual(insertionsort([96,67,64,37,105,78,102,55,54]),[37, 54, 55, 64, 67, 78, 96, 102, 105])
assertEqual(insertionsort([9,5,7,8,3,5,6,1,9,5,6,2]),[1, 2, 3, 5, 5, 5, 6, 6, 7, 8, 9, 9])
assertEqual(insertionsort([10,35,20,15,13,80,60,53,42,52]),[10, 13, 15, 20, 35, 42, 52, 53, 60, 80])

#Part B

def insertionsort_rec(ilist,index=1):

    """

    This function will preform the insertionsort sorting
    algorithm through a recursive function.

    ilist -- unsorted list of integers
    index -- integer

    return -- sorted list of integers

    """
    
    if index >= len(ilist):
        return ilist
    if ilist[index-1] > ilist[index]:
        variable = ilist[index]
        for ele in range(0, index): 
            if variable < ilist[ele]:
                ilist.insert(ele,variable)
                del ilist[index+1]
                break
    return insertionsort_rec(ilist, index+1)

# The non recsive function was more easily implemented.
# It is easier to work with ranges to sequentially scan a list
# rather than have the function recursivley do it in this situation.
    


assertEqual(insertionsort_rec([96,67,64,37,105,78,102,55,54]),[37, 54, 55, 64, 67, 78, 96, 102, 105])
assertEqual(insertionsort_rec([9,5,7,8,3,5,6,1,9,5,6,2]),[1, 2, 3, 5, 5, 5, 6, 6, 7, 8, 9, 9])
assertEqual(insertionsort_rec([10,35,20,15,13,80,60,53,42,52]),[10, 13, 15, 20, 35, 42, 52, 53, 60, 80])

#Problem 4

"""

Concepts: Employee, Car, Rectangle

Employee Attributes: Name,Position,Salary
Employee Functions:Change Salary, Promote/Demote Position,Change Name

Car Attributes: Color, Make, Model
Car Functions: Drive, Re-fuel, Turn

Rectange Attributes:Color,Size,Area
Rectangle Functions: Change Width, Change Length, Change Color

"""

#Problem 5

class time:
    
    """

    Time is desribed as seconds, minutes, and hours that tell
    you the point of day.

    seconds -- integer
    minutes -- integer
    hour - integer

    """

    def __init__(self,hour,minute,second):
        self.second = second
        self.minute = minute
        self.hour = hour

    """

    def time_function(aTime):
        return aTime.second
               aTime.minute
               aTime.hour
    """
                 
    def time_difference(time1,time2):
        
        """

        This function will take two times and tell you the
        difference between the two.

        time1 - integer
        time2 - integer

        return integer

        """
        
        time_dif_hour = (time1.hour - time2.hour) * 3600
        time_dif_minute = (time1.minute - time2.minute) * 60
        time_dif_seconds = (time1.second - time2.second)

        return abs(time_dif_hour + time_dif_minute + time_dif_seconds)
        

time1 = time(5,30,45)
time2 = time(4,30,15)
time3 = time(3,15,10)
time4 = time(10,25,45)

assertEqual(time.time_difference(time1,time2),3630)
assertEqual(time.time_difference(time4,time3),25835)
assertEqual(time.time_difference(time4,time1),17700)

#Problem 6

class threeletter:
    
    """

    This class will represent only three letter words.

    word -- string
    definition -- string

    """

    def __init__(self,word,definition):
        self.word = word
        self.definition = definition

    """

    def threeletter_function(word,definition,chars):
        return threeletter.word
               threeletter.definition
               threeletter.chars
    """
    def letterin(word,letter):

        """

        This function will check if the letter provided appears
        in a word

        word -- string
        letter -- string

        """
        
        if (len(word.word) != 3):
            return False
        elif letter not in word.word:
            return False
        if letter in word.word:
            return True

word1 = threeletter('abs','an abdominal muscle')
word2 = threeletter('car','a motor vehicle')
word3 = threeletter('jar','a container')
    
assertEqual(threeletter.letterin(word1,'a'),True)
assertEqual(threeletter.letterin(word2,'b'),False)
assertEqual(threeletter.letterin(word3,'r'),True)

#Problem 7

class quadratic:
    
    """

    This class will be used to represent the left hand side of the quadratic
    equation witch has variales a,b,c.

    a - integer
    b - integer
    c - integer
    
    """
    
    def __init__(self,a,b,c):

        self.a = a
        self.b = b
        self.c = c
        
    """

    def quadratic_function(shape,x):
        return quadratic.a
               quadratic.b
               quadratic.c
            
    """
   
    def evaluate_quadratic(shape,x):
        
        """

        This function will evaluate the quadratic equation
        when given a shape along with a seperate value x.

        shape -- shape
        x -- integer

        return integer

        """
        
        d = ((shape.a*x)** 2) + (shape.b * x) + shape.c
        return d
        
shape1 = quadratic(3,4,5)
shape2 = quadratic(1,3,5)
shape3 = quadratic(4,5,6)

assertEqual(quadratic.evaluate_quadratic(shape1,3),98)
assertEqual(quadratic.evaluate_quadratic(shape2,3),23)
assertEqual(quadratic.evaluate_quadratic(shape3,3),165)

#Problem 8

class Student:
    
    """

    Students are people who attend a school. They are a human being that
    have a first and last name, major, GPA, and year level.

    first -- string
    last -- string
    major -- string
    GPA -- integer
    year -- string

    """

    def __init__(self,first,last,major,GPA,year):
        self.first = first
        self.last = last
        self.major = major
        self.GPA = GPA
        self.year = year

    """

    def Student_function(aStudent,..)
        return Student.first
               Student.last
               Student.major
               Student.GPA
               Student.year
    """
    
    def check_year(student):
        
        """

        This function will take a student and return the current
        year they are in.

        student -- Student

        return -- string

        """
        return student.year
    
    def isComputerScience(student):

        """

        This function will check if the requested student has a major
        of computer science.

        Student -- Student

        return -- boolean

        """
        if (student.major == 'Computer Science'):
            return True
        else:
            return False
        
Student1 = Student('Joe','Guarni','Computer Engineering',3.7,'Junior')
Student2 = Student('Bob','Jones','Computer Science',3.0,'Freshman')
Student3 = Student('Dave','Williams','Biology',3.2,'Senior')
Student4 = Student('Maria','Smith','Political Science',3.4,'Senior')

assertEqual(Student.check_year(Student1),'Junior')
assertEqual(Student.check_year(Student2),'Freshman')
assertEqual(Student.isComputerScience(Student3),False)
assertEqual(Student.isComputerScience(Student2),True)


#Problem 9

def userinput(atext):
    
    """

    This function will check if what the user inputted is a single
    alpha character. The function will keep going while the user
    enters numbers, multi-char strings, and special characters.
    

    atext -- could be string,integer,float

    return -- string

    """

    #This is how the program ends. When the user types 0 thier word is completed
    #and the function returns 0 to the main signaling the end of a word.
    
    while (atext == '0'):
        print('Word Completed! \n')
        return '0'
    
    #This statement checks if atext is an alpha character, does not equal 0, and is only a single character.
    while not atext.isalpha() and (atext != '0') or (len(atext) > 1): 
            
        print('That is not a letter')
        atext = input('Please enter another letter: ').lower()
    return atext #returns

utext = userinput(input("Please Enter a letter: "))


"""

If method is written inside the class
    objectname.method()
if method is written outside the class
    method(objectname)

def __str__(self):
    return "The student name is" + self.name + "and her gpa is" + str(self.gpa)


To make an attribute private....
Use -- self.__name = name


Accessing private objects..

    def get_name(self):
         return self.__name
    def get_gpa(self):
         return self.__gpa
    def set_name(self, newname):
         self.__name = newname
    def set_gpa(self, newgpa):
         self.__gpa == newgpa

Defining subclasses

class HonorStudent(Student):
 
     def_init__(self,fancy,show-off):
          studnent.__init__(self,name,gpa)
          self.__fancy = fancy
          self.__showoff = showoff
"""
