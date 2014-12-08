#Lab 8
#CISC106 - 7/29/13
#Joe Guarni

from cisc106 import *

class Electronics:
    
    """

    An electronic is a device that uses electricity to display information.
    THe electronics in ComputersRus have a barcode,price,description and quantity.

    barcode -- integer
    price -- integer
    description -- string
    quantity -- integer
    
    """
    def __init__(self,barcode,price,description,quantity):
        self.__barcode = barcode
        self.__price = price
        self.__description = description
        self.__quantity = quantity

    """

    def Electronics_function(aElectronic):
        retrun Electronics.barcode
               Electronics.price
               Electronics.description
               Electronics.quantity


    """

    #The Following functions set and get the private attributes of the class
    def getBarcode(self):
        return self.__barcode
    def getPrice(self):
        return self.__price
    def getDescription(self):
        return self.__description
    def getQuantity(self):
        return self.__quantity
    def setBarcode(self,newbarcode):
        self.__barcode = newbarcode
    def setPrice(self,newprice):
        self.__price = newprice
    def setDescription(self,newdescription):
        self.__description = newdescription
    def setQuantity(self,newquantity):
        self.__quantity = newquantity

    def update_stock(self,nproducts):

        """

        This function will add a given quantity of products to
        the inventory of a type of electronic.

        nproducts -- integer

        return -- integer[updates self.quantity]

        """

        self.__quantity = self.__quantity + nproducts
        return self.__quantity
        

    def calculate_inventory(self):

        """

        This function will return the money the store
has in a given
        product’s inventory.

        return -- integer

        """
        
        return self.__quantity * self.__price
        

class TV(Electronics):
    
    """

    A TV is an electronic that has a barcode,price,description,quantity,model and a size.
    It is a subclass of the superclass Electronics.

    model -- string
    size -- integer
    
    """
    
    def __init__(self,barcode,price,description,quantity,model,size):
        Electronics.__init__(self,barcode,price,description,quantity)
        self.__model = model
        self.__size = size

    """

    def TV_function(aTV):
        return TV.model
               TV.size

    """
    
    #The Following functions set and get the private attributes of the class
    def getModel(self):
        return self.__model
    def getSize(self):
        return self.__size
    def setModel(self,newmodel):
        self.__model = newmodel
    def setSize(self,newsize):
        self.__size = newsize

class Computers(Electronics):

    """

    A Computer is an electronic that has a barcode,price,description,quantity,ram,processor
    speed,and hard drive capactiy. It is a subclass of the superclass electronics.

    ram -- integer
    processor -- string
    speed -- integer
    capacity -- integer

    """
    
    def __init__(self,barcode,price,description,quantity,ram,processor,speed,capacity):
        Electronics.__init__(self,barcode,price,description,quantity)
        self.__ram = ram
        self.__processor = processor
        self.__speed = speed
        self.__capacity = capacity

    """

    def Computers_function(aComputer):
        return Computers.ram
               Computers.processor
               Computers.speed
               Computers.capacity

    """
    
    #The Following functions set and get the private attributes of the class
    def getRam(self):
        return self.__ram
    def getProcessor(self):
        return self.__processor
    def getSpeed(self):
        return self.__speed
    def getCapacity(self):
        return self.__capacity
    def setRam(self,newram):
        self.__ram = newram
    def setProcessor(self,newprocessor):
        self.__processor = newprocessor
    def setSpeed(self,newspeed):
        self.__speed = newspeed
    def setCapacity(self,newcapacity):
        self.__capacity = newcapacity

class Camera(Electronics):

    """

    A camera is a device that has a barcode,price,description,quantity,pixels and is a
    subclass of the superclass Electronics.

    pixels -- integer

    """
    
    def __init__(self,barcode,price,description,quantity,pixels):
        Electronics.__init__(self,barcode,price,description,quantity)
        self.__pixels = pixels

    """

    def Camera_function(aCamera):
         return Camera.pixels

    """
    
    #The Following functions set and get the private attributes of the class       
    def getPixels(self):
        return self.__pixels
    def setPixels(self,newpixels):
        self.__pixels = newpixels

def main():

    """

    This is the main function of the program. It will create the objects necessary
    to test each class for validity. It will also run the assertEqual tests to make
    sure teh class functions work properly.

    """
    
    tv_version1 = TV(565,1000,"Black",10,'Plasma',37)
    tv_version2 = TV(392,1500,"Grey",12,"LCD",42)
    
    camera_version1 = Camera(242,500,"Black",3,1000)
    camera_version2 = Camera(453,750,"Neon",6,1500)

    computer_version1 = Computers(787,1200,"Silver",100,4,"i5",2.66,500)
    computer_version2 = Computers(866,1500,"Grey",50,8,"i7",2.75,250)
    
    assertEqual(Electronics.calculate_inventory(tv_version1),10000)
    assertEqual(Electronics.calculate_inventory(camera_version1),1500)
    assertEqual(Electronics.calculate_inventory(computer_version1),120000)

    assertEqual(Electronics.update_stock(tv_version1,15),25)
    assertEqual(Electronics.update_stock(computer_version1,100),200)
    assertEqual(Electronics.update_stock(camera_version1,10),13)
    
main()
