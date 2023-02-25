#Authors: Athanasios Kalogiratos

import random

#This class includes all the required methods for weapons
class weapons():
    def __init__(self) -> None:
        #Weapons are seprated into rifles and pistols lists
        self.rifles=["Automatic", "Semi Automatic", "Single Shot", "Bolt-Action Rifle", "Lever Action", "Break Action", "Pump Action"]
        self.pistols=["Single Shot", "Double Action Revolver", "Semi Automatic pistol"]
        
    #This method returns the rifles list
    def getRifles(self) -> list:
        return self.rifles
    
    #This method returns the pistols list
    def getPistols(self) -> list:
        return self.pistols
    
    #This method tries to add a new rifle into the list and prints a message accordingly
    def addRifle(self, rifle) -> None:
        try:
            self.rifles.append(rifle)
        except:
            print("Could not add rifle!")
        else:
            print("Rifle added!") 
    
    #This method tries to add a new rifle into the list and prints a message accordingly
    def addPistol(self, pistol) -> None:
        try:
            self.pistols.append(pistol)
        except:
            print("Could not add pistol!")
        else:
            print("Pistol added!") 
    
    #This method tries to remove a rifle from the rifle list and prints a message accordingly
    def removeRifle(self, rifle) -> None:
        try:
            self.rifles.remove(rifle)
        except:
            print("Could not remove rifle!")
        else:
            print("Rifle removed!")
          
    #This method tries to remove a pistol from the pistol list and prints a message accordingly        
    def removePistol(self, pistol) -> None:
        try:
            self.pistols.remove(pistol)
        except:
            print("Could not remove pistol!")
        else:
            print("Pistol removed!")
            
    
#This class includes all the required methods for accessories
class accessories():
    def __init__(self) -> None:
        #This is the list with all the available accessories
        self.accessories=["Jackets", "Pants", "Spats", "Belts", "Hats", "Boots", "Socks", "Torches"]
    
    #This method returns the accessories list    
    def getAccessories(self) -> list:
        return self.accessories
    
    #This method tries to add an accessory into the accessories list and prints a message accordingly
    def addAccessory(self, accessory) -> None:
        try:
            self.accessories.append(accessory)
        except:
            print("Could not add accessory!")
        else:
            print("Accessory added!") 
    #This method tries to remove an accessory from the list and prints a message accordingly
    def removeAccessory(self, accessory) -> None:
        try:
            self.accessories.remove(accessory)
        except:
            print("Could not remove accessory!")
        else:
            print("Accessory removed!") 
    

#This class includes all the required methods for accessories   
class food():
    def __init__(self) -> None:
        #This list includes all the food available
        self.food=["Bread", "Butter", "Eggs", "Honey", "Milk", "Beans", "Lentils", "Onions", "Potatos", "Pork", "Beef", "Chicken", "Pasta",
                   "Rice"]
        
    #This method returns the food list    
    def getFood(self) -> list:
        return self.food
    
    #This method tries to add a food into the food list and prints a message accordingly
    def addFood(self, food) -> None:
        try:
            self.food.append(food)
        except:
            print("Could not add food!")
        else:
            print("Food added!") 
    
    #This method tries to remove a food from the food list and prints a message accordingly
    def removeFood(self, food) -> None:
        try:
            self.food.remove(food)
        except:
            print("Could not remove food!")
        else:
            print("Food removed!")
    

#This class includes all the required methods for radar       
class radar():
    def __init__(self) -> None:
    #This list contains 0s and 1s in a random order with 0s being more
     self.radarState=[0, 1, 0, 0, 0, 0, 0, 0 ,0 ,1 ,0 ,0 ,0 ,0 ,0]
    
    #This method shuffles the list above and then picks the first element to present it as a result. 
    #Since we do not have a real radar sensor in a real enviroment we kind of simulate the readings we would get from one.
    #We make the assumption that the instances we will get a positive detection signal from the radar are way fewer than the instances we get one.
    def getRadarState(self) -> bool:
        random.shuffle(self.radarState)
        return(self.radarState[0]==1)
        
#This class includes all the required methods for vehicles
class vehicles():
    def __init__(self) -> None:
        #The lists below respectively contain the cars, trucks and armored vehicles that are available
        self.cars=["Land Cruiser", "Pajero", "Quasqai", "Navara", "Aventador", "G Wagon"]
        self.trucks=["Mercedes-Benz 1117", "Scania R 420", "EOD Duro II", "Ford Transit Minibus"]
        self.armored=["Mowag Piranha IIIH", "RG-32M Light Tactical Vehicle", "Ford F350 SRV"]
    
    #The get methods below return the cars, trucks, armored list respectively
    def getCars(self) -> list:
        return self.cars
    
    def getTrucks(self) -> list:
        return self.trucks
    
    def getArmored(self) -> list:
        return self.armored
    
    #The get methods below attempt respectively to add a new car, truck, armored vehicle into the respective list 
    def addCar(self, car) -> None:
        try:
            self.cars.append(car)
        except:
            print("Could not add car!")
        else:
            print("Car added!") 
    
    def addTruck(self, truck) -> None:
        try:
            self.trucks.append(truck)
        except:
            print("Could not add truck!")
        else:
            print("Truck added!") 
            
    def addArmored(self, armored) -> None:
        try:
            self.armored.append(armored)
        except:
            print("Could not add armored!")
        else:
            print("Armored added!") 
    
    #The get methods below attempt respectively to remove a car, truck, armored vehicle from the respective list 
    def removeCar(self, car) -> None:
        try:
            self.cars.remove(car)
        except:
            print("Could not remove car!")
        else:
            print("Car removed!") 
            
    def removeTruck(self, truck) -> None:
        try:
            self.trucks.remove(truck)
        except:
            print("Could not remove truck!")
        else:
            print("Truck removed!")
    
    def removeArmored(self, armored) -> None:
        try:
            self.armored.remove(armored)
        except:
            print("Could not remove armored!")
        else:
            print("Armored removed!") 

    