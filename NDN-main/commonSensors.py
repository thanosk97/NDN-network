#Authors: Jeremie Sajeev Daniel, Athanasios Kalogiratos(minor adjustments)  
import string
import random

#This class includes all the required methods for the Co2 sensor
class C02Sensor():
    
    ##Default percentage 0.04%
    def __init__(self) -> None:
        self.gasPercentage = 0.0004
        self.defaultGasPercentage = 0.0004
        
    #Returns the gas percentage
    def getGasPercentage(self) -> float:
        return self.gasPercentage

    #Calculates the gas percentage
    def calcGasPercentage(self,ventilation,personPresent) -> None:
        if ventilation is True:
            self.gasPercentage = max(self.gasPercentage-0.0001,self.defaultGasPercentage)
        else:
            self.gasPercentage += 0.00001*(personPresent+1)
            
    #This method prints a message depending on the gas.
    def getStatus(self) -> string:
        if (self.gasPercentage>=0.04):
            return "Immediate Danger to Life"
        elif (self.gasPercentage>=0.03):
            return "High Alarm"
        elif (self.gasPercentage>=0.015):
            return "Medium Alarm"
        elif (self.gasPercentage>=0.005):
            return "Low Alarm"
        else:
            return "Good"

#Temperature string estimates based on wikipedia
class TemperatureSensor():
    def __init__(self,temp) -> None:
        self.currentTemperature = temp
        self.projectedFutureTemp = temp
        
    #This method prints a message depending on the temperature
    def getStatus(self) -> string:
        if self.currentTemperature >= 28:
            return "Above Recommended Temeperature"
        elif self.currentTemperature >= 18:
            return "Ideal Temperature"
        else:
            return "Lower than Recommended Temperature"
    
    #This method is used to adjust the temperature
    def adjustTemeperature(self,projectedFutureTemp = None) -> None:
        if projectedFutureTemp != None:
            self.projectedFutureTemp = projectedFutureTemp
        if (self.currentTemperature>self.projectedFutureTemp):
            self.currentTemperature -= (self.currentTemperature-self.projectedFutureTemp)*0.2
        else:
            self.currentTemperature += (self.projectedFutureTemp-self.currentTemperature)*0.2

    #This temperature returns the value of the current temperature
    def getCurrentTemp(self) -> float:
        return self.currentTemperature
    
    #This returns the value of the desired temperature
    def getProjectedTemp(self) -> float:
        return self.projectedFutureTemp

#This method contains methods about the peoples count
class MembersCount():
    #Default number of military's and civilians
    def __init__(self) -> None:
        self.militaryPersonnel = 0
        self.civillianPersonnel = 0

    #This method adds a member either on the military personnel or civillian 
    def memberCheckIn(self, militaryMember) -> None:
        if militaryMember is True:
            self.militaryPersonnel+=1
        else:
            self.civillianPersonnel+=1
            
    #This method removes a member either out of the military personnel or civillian 
    def memberCheckOut(self,militaryMember) -> None:
        if militaryMember is True:
            if self.militaryPersonnel>0:
                self.militaryPersonnel-=1
        else:
            if self.civillianPersonnel>0:
                self.civillianPersonnel-=1

    #This method returns the number of civillian personnel in the base
    def getCivilianCount(self) -> int:
        return self.civillianPersonnel

    
    #This method returns the number of military personnel in the base
    def getMilitaryCount(self) -> int:
        return self.militaryPersonnel

    #This method returns the number of civillian and military personnel combined
    def getTotalPeople(self) -> int:
        return self.militaryPersonnel + self.civillianPersonnel

#Checks if confidential boxes were opened
class LightProtoSensor():
    #Define empty set of boxes
    def __init__(self) -> None:
        self.protoSensors = {}
    #Method to add sensor
    def addSensor(self,box):
        self.protoSensors[box] = 1
    #Method to check if a box is opened
    def boxOpened(self,box):
        if box in self.protoSensors:
            self.protoSensors[box] = 0
    #Method to check if box is closed
    def checkBoxClosed(self,box):
        if box in self.protoSensors:
            return self.protoSensors[box] == 1
        else:
            return None
    #MEthod removes sensor from the set
    def removeSensor(self,box):
        if box in self.protoSensors:
            self.protoSensors.pop(box)

#This class contains methods and data about the motion sensors
class MotionSensor():
    def __init__(self) -> None:
        #Empty cameras set 
        self.cameras = {}
        #A list containing numbers from 0 to 360 with a step of 15
        self.degrees=list(range(0, 360, 15))
    
    #This method prints the camera and the angle that detwcted a movement
    def cameraMotion(self):
        for x in self.cameras:
            random.shuffle(self.degrees)
            #chance of motion -- will need some rng here to emulate motion detection
            if (random.randint(1,5)%2==0):
                self.cameras[x]= "Movement at " + x + " camera at " + str(self.degrees[0]) + " angle"
            else:
                self.cameras[x]= "Movement is not detected"
    #Thism ethod adds a camera
    def addCamera(self,x):
        self.cameras[x] = 0
        
    #This method removes a camera
    def removeCam(self,x):
        if x in self.cameras:
            self.cameras.pop(x)
            
    #this method checks if a camera exists in the system
    def checkCamera(self,x):
        if x in self.cameras:
            return self.cameras[x]
        else:
            return None

    



#Vibration Sensor
class VibrationSensor():
    def __init__(self) -> None:
        #Empty set of vibration sensors
        self.vibrationSensors = {}
        #Numbers from 0 to 100 with a step of 15
        self.vibrationValues=list(range(0, 100, 5))
    
    #This method returns the state of a vibration sensor
    def getVibrationSensorState(self) -> None:
        for x in self.vibrationSensors:
            random.shuffle(self.vibrationValues)
            if (self.vibrationValues[0] > 75):
                self.vibrationSensors[x]="Suspicious vibration at " + x
            else:
                self.vibrationSensors[x] = "Vibration not found"
    
    #Adds sensor
    def addSensor(self,x):
        self.vibrationSensors[x] = 0
    
    #Checks if the vibration exists in the system
    def checkVibrationSensor(self,x):
        if x in self.vibrationSensors:
            return self.vibrationSensors[x]
        else:
            return None

    #Removes sensor from the system
    def removeSensor(self,x):
        if x in self.vibrationSensors:
            self.vibrationSensors.pop(x)



#Sound Sensors
class SoundSensor():
    def __init__(self) -> None:
        #Empty set of sound sensors
        self.soundSensors = {}
        #A list/map of db levels
        self.soundSensorDB=[30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 70, 73, 75, 77, 80, 90, 100]
    
    #Returns the state of a particular sound sensor
    def getSoundSensorState(self) -> None:
        for x in self.soundSensors:
            random.shuffle(self.soundSensorDB)
            if (self.soundSensorDB[0] >= 80):
                 self.soundSensors[x]="Suspicious sound at "+ x
            else:
                self.soundSensors[x] = 'No sound found'

    #Adds a sound sensor
    def addSensor(self,x):
        self.soundSensors[x] = 0

    #Removes a sound sensor 
    def removeSensor(self,x):
        if x in self.soundSensors:
            self.soundSensors.pop(x)
    
    #Retreives a sound sensor
    def getSensor(self,x):
        if x in self.soundSensors:
            return self.soundSensors[x]
        else:
            return None

