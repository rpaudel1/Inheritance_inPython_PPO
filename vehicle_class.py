## Vehicle_class.py is the module which will be imported
class Automobile: # super-class
  #Constructor method
  def __init__(self, make, model, year, mileage, price):
    self.__make = make
    self.__model = model
    self.__year = year
    self.__mileage = mileage
    self.__price = price
  #Mutators methods
  def set_make(self, make):
    self.__make = make
  def set_model(self, model):
    self.__model = model
  def set_year(self, year):
    self.__year = year
  def set_mileage(self, mileage):
    self.__mileage = mileage
  def set_price(self, price):
    self.__price = price

  #Accessor methods
  def get_make(self):
    return self.__make
  def get_model(self):
    return self.__model
  def get_year(self):
    return self.__year
  def get_mileage(self):
    return self.__mileage
  def get_price(self):
    return self.__price
  def __str__(self): #String method
    return 'The maker of the vehicle is: ' + self.get_make() + \
    '\nThe model of the vehicle is: ' + self.get_model() +  \
    '\nThe year of the vehicle is: ' + str(self.get_year()) + \
    '\nThe mileage of the vehicle is: ' + str(self.get_mileage())+\
    '\nThe price of the vehicle is: ' + str(self.get_price())
# Subclass Car
class Car(Automobile):
  def __init__(self, make, model, year, mileage, price, doors):
    Automobile.__init__(self, make, model, year, mileage, price) # inherit
    self.__doors = doors

  def set_doors(self, doors):
    self.__doors = doors
  def get_doors(self):
    return self.__doors

#Subclass Truck    
class Truck(Automobile):
  def __init__(self, make, model, year, mileage, price, drive_type):
    Automobile.__init__(self, make, model, year, mileage, price) #inherit
    self.__drive_type = drive_type
        
  def set_drive_type(self, drive_type):
    self.__drive_type = drive_type
  def get_drive_type(self):
    return self.__drive_type
    
#Subclass SUV
class SUV(Automobile):
  def __init__(self, make, model, year, mileage, price, pass_cap):
    Automobile.__init__(self, make, model, year, mileage, price)
    self.__pass_cap = pass_cap

  def set_pass_cap(self, pass_cap):
    self.__pass_cap = pass_cap
  def get_pass_cap(self):
    return self.__pass_cap
  
        
