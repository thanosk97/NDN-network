#Authors: Athanasios Kalogiratos, Jeremie Sajeev Daniel, Yue Ding

from packets import DataPacket, InterestPacket
from sendInterest import SendInterest
from commonSensors import C02Sensor,TemperatureSensor,LightProtoSensor,MotionSensor,MembersCount,SoundSensor,VibrationSensor
import uniqueSensors
import socket
import base64
import traceback
import time
import threading

PEER_PORT = 33301    # Port for listening to other peers
SENSOR_PORT = 33401  # Port for listening to other sensors
ROUTER_HOST = '10.35.70.43'
BACKUP_ROUTER_HOST = '10.35.70.42'
ROUTER_PORT = 33344
# /*v* - Token Value for variables
advertise_string = '[weapon/co2/getGas, weapon/co2/getStatus, weapon/temp/getStatus, weapon/temp/adjustTemp/*v*, weapon/temp/getCurrentTemp, weapon/temp/getProjectedTemp, \
 weapon/members/checkIn/*v*, weapon/members/checkOut/*v*, weapon/members/getCivillianCount, weapon/members/getMilitaryCount, weapon/members/getTotalPeople, \
 weapon/lpSensor/addSensor/*v*, weapon/lpSensor/boxOpen/*v*, weapon/lpSensor/checkBox/*v*, weapon/lpSensor/removeSensor/*v*, \
 weapon/motionSensor/addCamera/*v*, weapon/motionSensor/removeCamera/*v*, weapon/motionSensor/checkCamera/*v*, \
 weapon/vibrationSensor/addSensor/*v*, weapon/vibrationSensor/checkVibrationSensor/*v*, weapon/vibrationSensor/removeSensor/*v*, \
 weapon/soundSensor/addSensor/*v*, weapon/soundSensor/getSensor/*v*, weapon/soundSensor/removeSensor/*v*, \
 weapon/weapons/getRifles, weapon/weapons/getPistols, weapon/weapons/addRifle/*v*, weapon/weapons/addPistol/*v*, weapon/weapons/removeRifle/*v*, weapon/weapons/removePistol/*v*]'
 
BARRACK_TYPE = 'weapon' # weapon,vehicle,accessory,radar,food
class Barrack():
    class Peer:
        def __init__(self, host, port):
            self.host = host
            self.port = port
            self.peers = set()

        def advertiseFeature(self):
            """Advertise the host IP."""
            server_tup = (ROUTER_HOST, ROUTER_PORT)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect(server_tup)
            except:
                server_tup = (BACKUP_ROUTER_HOST, ROUTER_PORT)
            message = f'HOST {self.host} PORT {self.port} ACTION {advertise_string}'
            print('Advertising ', message)
            s.send(message.encode())
            s.close()

    
    def bencode(self,toEncode):
        """Encode with Base64"""
        dp = DataPacket()
        toEncode1 = dp.encodeData(toEncode)
        ascii_encoded = toEncode1.encode("ascii")
        base64_bytes = base64.b64encode(ascii_encoded)
        base64_string = base64_bytes.decode("ascii")
        return base64_string

    def bdecode(self,toDecode):
        """Decode with Base64"""
        base64_bytes = toDecode.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")
        ip = InterestPacket()
        sample_string = ip.decodeData(sample_string)
        return sample_string

    def sendAck(self,conn, raddr, result):
            """Send sensor data to all peers."""
            try:
                # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # s.connect((raddr, SENSOR_PORT))
                msg = result
                conn.send(self.bencode(msg).encode())
                # sent = True
                # s.close()
            except Exception:
                print(traceback.format_exc())
                print('exception occurred while sending acknowledgement: ', Exception)
                
            
    def callActuator1(self,interest,interest_method,interest_variable):
        """Call the actuator of the method apart from get method"""
        # Adjust temperature 
        if interest.lower() == 'temp' and interest_method.lower() == 'adjusttemp':
            try:
                self.temp.adjustTemeperature(float(interest_variable))
                return "ACTION COMPLETED"
            except:
                return "Unknown Data Type action not performed"

        # Checkin military member
        elif interest.lower() == 'members' and interest_method.lower() == 'checkin':
            if (interest_variable.lower()=='true'):
                self.memberscount.memberCheckIn(True)
            else:
                self.memberscount.memberCheckIn(False)
            return "ACTION COMPLETED"

        # Checkout military member
        elif interest.lower() == 'members' and interest_method.lower() == 'checkout':
            if (interest_variable.lower()=='true'):
                self.memberscount.memberCheckOut(True)
            else:
                self.memberscount.memberCheckOut(False)
            return "ACTION COMPLETED"

        # Light Proto Sensor
        elif interest.lower() == 'lpsensor' and interest_method.lower() == 'addsensor':
            self.lpsensors.addSensor(interest_variable)
            return "ACTION COMPLETED"
        elif interest.lower() == 'lpsensor' and interest_method.lower() == 'boxopen':
            self.lpsensors.boxOpened(interest_variable)
            return "ACTION COMPLETED"
        elif interest.lower() == 'lpsensor' and interest_method.lower() == 'checkbox':
            status = self.lpsensors.checkBoxClosed(interest_variable)
            if (status != None):
                if (status):
                    return "Box Hasn't been opened"
                else:
                    return "Box has been opened"
            else:
                return "Box doesn't have a sensor"

        # Motion sensor
        elif interest.lower() == 'motionsensor' and interest_method.lower() == 'addcamera':
            self.msensors.addCamera(interest_variable)
            return "ACTION COMPLETED"
        elif interest.lower() == 'motionsensor' and interest_method.lower() == 'removecamera':
            self.msensors.removeCam(interest_variable)
            return "ACTION COMPLETED"
        elif interest.lower() == 'motionsensor' and interest_method.lower() == 'checkcamera':
            self.msensors.cameraMotion()
            status = self.msensors.checkCamera(interest_variable)
            if (status != None):
                return status
            else:
                return "No camera at location"

        # Vibration sensor
        elif interest.lower() == 'vibrationsensor' and interest_method.lower() == 'addsensor':
            self.vibrationSensor.addSensor(interest_variable)
            return "ACTION COMPLETED"
        elif interest.lower() == 'vibrationsensor' and interest_method.lower() == 'removesensor':
            self.vibrationSensor.removeSensor(interest_variable)
            return "ACTION COMPLETED"
        elif interest.lower() == 'vibrationsensor' and interest_method.lower() == 'checkvibrationsensor':
            self.vibrationSensor.getVibrationSensorState()
            status = self.vibrationSensor.checkVibrationSensor(interest_variable)
            if (status != None):
                return status
            else:
                return "No vibration sensor at location"

        # Sound sensor         
        elif interest.lower() == 'soundsensor' and interest_method.lower() == 'addsensor':
            self.soundSensor.addSensor(interest_variable)
            return "ACTION COMPLETED"
        elif interest.lower() == 'soundsensor' and interest_method.lower() == 'removesensor':
            self.soundSensor.removeSensor(interest_variable)
            return "ACTION COMPLETED"
        elif interest.lower() == 'soundsensor' and interest_method.lower() == 'getsensor':
            self.soundSensor.getSoundSensorState()
            status = self.soundSensor.getSensor(interest_variable)
            if (status != None):
                return status
            else:
                return "No sound sensor at location"

        # Unique sensor - weapons
        elif interest.lower() == 'weapons' and interest_method.lower() == 'addrifle':
            self.uniqueSens.addRifle(interest_variable)
            return "ACTION COMPLETED"
        elif interest.lower() == 'weapons' and interest_method.lower() == 'addpistol':
            self.uniqueSens.addPistol(interest_variable)
            return "ACTION COMPLETED"
        elif interest.lower() == 'weapons' and interest_method.lower() == 'removerifle':
            self.uniqueSens.removeRifle(interest_variable)
            return "ACTION COMPLETED"
        elif interest.lower() == 'weapons' and interest_method.lower() == 'removepistol':
            self.uniqueSens.removePistol(interest_variable)
            return "ACTION COMPLETED"
        
        return "Nothing Called"
        
        
        
    def callActuator(self,interest,interest_method):
        """Call the actuator of the get method"""
        # Get percentage of CO2
        if interest.lower() == 'co2' and interest_method.lower() == 'getgas':
            self.co2.calcGasPercentage(self.ventilation,self.memberscount.getTotalPeople())
            return self.co2.getGasPercentage()

        # Get status of CO2
        elif interest.lower() == 'co2' and interest_method.lower() == 'getstatus':
            self.co2.calcGasPercentage(self.ventilation,self.memberscount.getTotalPeople())
            return self.co2.getStatus()

        # Get status of temperature
        elif interest.lower() == 'temp' and interest_method.lower() == 'getstatus':
            self.temp.adjustTemeperature()
            return self.temp.getStatus()

        # Get current temperature
        elif interest.lower() == 'temp' and interest_method.lower() == 'getcurrenttemp':
            self.temp.adjustTemeperature()
            return self.temp.getCurrentTemp()
        
        # Get projected temperature
        elif interest.lower() == 'temp' and interest_method.lower() == 'getprojectedtemp':
            return self.temp.getProjectedTemp()
        
        # Get number of civillian
        elif interest.lower() == 'members' and interest_method.lower() == 'getcivilliancount':
            return self.memberscount.getCivilianCount()

        # Get number of military
        elif interest.lower() == 'members' and interest_method.lower() == 'getmilitarycount':
            return self.memberscount.getMilitaryCount()

        elif interest.lower() == 'members' and interest_method.lower() == 'gettotalpeople':
            return self.memberscount.getTotalPeople()

        # Unique sensor - weapons
        elif interest.lower() == 'weapons' and interest_method.lower() == 'getrifles':
            return self.uniqueSens.getRifles()
        elif interest.lower() == 'weapons' and interest_method.lower() == 'getpistols':
            return self.uniqueSens.getPistols()

        return "Nothing Called"

    def receiveData(self):
        """Listening to the requests from other barracks"""
        print("listening for actuation requests")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hostname = socket.gethostname()
        host = socket.gethostbyname(hostname)
        port = PEER_PORT
        s.bind((host, port))
        s.listen(5)
        while True:
            conn, addr = s.accept()
            print("addr: ", addr[0])
            # print("connection: ", str(conn))
            data = conn.recv(1024)
            data = self.bdecode(data.decode())
            print(data, " to actuate on")
            # call actuators
            barrack_type, interest, interest_method, interest_variable = None, None, None, None
            try:
                [barrack_type, interest,interest_method, interest_variable] = data.split('/')
            except:
                [barrack_type, interest,interest_method] = data.split('/')
            if BARRACK_TYPE == barrack_type:
                if (interest_variable is None):
                    actuationResult = self.callActuator(interest, interest_method)
                else:
                    actuationResult = self.callActuator1(interest, interest_method,interest_variable)
            self.sendAck(conn, addr[0], str(actuationResult))
            conn.close()
            time.sleep(1)

    def main(self):
        # parser = argparse.ArgumentParser()
        # #Barrack options 1-5 for 5 unique models
        # parser.add_argument('--o', help='Barrack options', type=int)
        # args = parser.parse_args()

        # if args.o is None or args.o>=6 or args.o<1:
        #     print("Please specify which barrack is being looked at: (1-5)")
        #     exit(1)
        # uniqueSens = None
        # if args.o == 1:
        #     uniqueSens = uniqueSensors.weapons()
        # elif args.o == 2:
        #     uniqueSens = uniqueSensors.accessories()
        # elif args.o == 3:
        #     uniqueSens = uniqueSensors.vehicles()
        # elif args.o == 4:
        #     uniqueSens = uniqueSensors.radar()
        # else:
        #     uniqueSens = uniqueSensors.food()
        self.uniqueSens = uniqueSensors.weapons()
        self.co2 = C02Sensor()
        #default temperature
        self.temp = TemperatureSensor(21)
        self.lpsensors = LightProtoSensor()
        self.msensors = MotionSensor()
        self.memberscount = MembersCount()
        self.soundSensor = SoundSensor()
        self.vibrationSensor = VibrationSensor()

        self.vibrationSensor.addSensor("North Entrance")
        self.vibrationSensor.addSensor("East Entrance")
        self.vibrationSensor.addSensor("South Entrance")
        self.vibrationSensor.addSensor("West Entrance")

        self.soundSensor.addSensor("North Entrance")
        self.soundSensor.addSensor("East Entrance")
        self.soundSensor.addSensor("South Entrance")
        self.soundSensor.addSensor("West Entrance")

        self.msensors.addCamera("North Entrance")
        self.msensors.addCamera("East Entrance")
        self.msensors.addCamera("South Entrance")
        self.msensors.addCamera("West Entrance")

        self.lpsensors.addSensor("Box 1")
        self.lpsensors.addSensor("Box 2")
        self.lpsensors.addSensor("Box 3")
        self.lpsensors.addSensor("Box 4")
        self.lpsensors.addSensor("Box 5")
        self.lpsensors.addSensor("Box 6")
        self.lpsensors.addSensor("Box 7")

        self.temp.adjustTemeperature(24)
        #First is military personnel then civiliian
        for x in range(100):
            self.memberscount.memberCheckIn(True)
        for x in range(10):
            self.memberscount.memberCheckIn(False)
        self.ventilation = True
        self.co2.calcGasPercentage(self.ventilation,self.memberscount.getTotalPeople())

        hostname = socket.gethostname()
        host = socket.gethostbyname(hostname)
        peer = self.Peer(host, PEER_PORT)
        t1 = threading.Thread(target=peer.advertiseFeature)
        si = SendInterest()

        t2 = threading.Thread(target=si.main)
        while True:
            t1.start()
            t2.start()
            self.receiveData()    




if __name__ == '__main__':
    barrack = Barrack()
    barrack.main()