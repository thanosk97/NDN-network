#Author: Ketan Anil Patil

import socket
import time
import base64
from packets import InterestPacket,DataPacket
ROUTER_IP = '10.35.70.43'
ROUTER_PORT = 33310

#main sendinterest class
class SendInterest:
    #Encodes a given string
    def bencode(self,toEncode):
        ip = InterestPacket()
        toEncode1 = ip.encodeData(toEncode)
        ascii_encoded = toEncode1.encode("ascii")
        base64_bytes = base64.b64encode(ascii_encoded)
        base64_string = base64_bytes.decode("ascii")
        return base64_string

    #Decodes a given string
    def bdecode(self,toDecode):
        base64_bytes = toDecode.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")
        dp = DataPacket()
        sample_string1 = dp.decodeData(sample_string)
        return sample_string1

    #Method includes everything related to the interest package "translation". It receives the interest package
    #and depending on the content prints the correct message by receiving information from the correct barrack and method
    def actuate(self,interest_packet, data_packet):
        print("Data packet received: ", data_packet, ' for interest packet ', interest_packet)
        barrack_type = interest_packet.split('/')
        if interest_packet == 'weapon/co2/getGas' or interest_packet == 'accessory/co2/getGas' or interest_packet == 'vehicle/co2/getGas' or interest_packet == 'food/co2/getGas' or interest_packet == 'radar/co2/getGas':
            print('Current Gas Percentage from ', barrack_type[0], ' is ', data_packet)
        elif interest_packet == 'weapon/co2/getStatus' or interest_packet == 'accessory/co2/getStatus' or interest_packet == 'vehicle/co2/getStatus' or interest_packet == 'food/co2/getStatus' or interest_packet == 'radar/co2/getStatus':
            print('Current Status of Gas of ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/temp/getStatus' or interest_packet == 'accessory/temp/getStatus' or interest_packet == 'vehicle/temp/getStatus' or interest_packet == 'food/temp/getStatus' or interest_packet == 'radar/temp/getStatus':
            print('Current Temperature status of Barrack ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/temp/adjustTemp/*v*' or interest_packet == 'accessory/temp/adjustTemp/*v*' or interest_packet == 'vehicle/temp/adjustTemp/*v*' or interest_packet == 'food/temp/adjustTemp/*v*' or interest_packet == 'radar/temp/adjustTemp/*v*':
            print('Temperature adjusted to ', data_packet, ' in Barrack ',barrack_type[0])
        elif interest_packet == 'weapon/temp/getCurrentTemp' or interest_packet == 'accessory/temp/getCurrentTemp' or interest_packet == 'vehicle/temp/getCurrentTemp' or interest_packet == 'food/temp/getCurrentTemp' or interest_packet == 'radar/temp/getCurrentTemp':
            print('Current Temperature reading in ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/temp/getProjectedTemp' or interest_packet == 'accessory/temp/getProjectedTemp' or interest_packet == 'vehicle/temp/getProjectedTemp' or interest_packet == 'food/temp/getProjectedTemp' or interest_packet == 'radar/temp/getProjectedTemp':
            print('Projected Temperature of', barrack_type[0], ':  ', data_packet)
        elif interest_packet == 'weapon/members/checkIn/*v*' or interest_packet == 'accessory/members/checkIn/*v*' or interest_packet == 'vehicle/members/checkIn/*v*' or interest_packet == 'food/members/checkIn/*v*' or interest_packet == 'radar/members/checkIn/*v*':
            print('Member Check-In in Barrack ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/members/checkOut/*v*' or interest_packet == 'accessory/members/checkOut/*v*' or interest_packet == 'vehicle/members/checkOut/*v*' or interest_packet == 'food/members/checkOut/*v*' or interest_packet == 'radar/members/checkOut/*v*':
            print('Member Check-Out in Barrack', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/members/getCivillianCount' or interest_packet == 'accessory/members/getCivillianCount' or interest_packet == 'vehicle/members/getCivillianCount' or interest_packet == 'food/members/getCivillianCount' or interest_packet == 'radar/members/getCivillianCount':
            print('Number of civilians present in Barrack ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/members/getMilitaryCount' or interest_packet == 'accessory/members/getMilitaryCount' or interest_packet == 'vehicle/members/getMilitaryCount' or interest_packet == 'food/members/getMilitaryCount' or interest_packet == 'radar/members/getMilitaryCount':
            print('Number of Military Personnel in Barrack ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/members/getTotalPeople' or interest_packet == 'accessory/members/getTotalPeople' or interest_packet == 'vehicle/members/getTotalPeople' or interest_packet == 'food/members/getTotalPeople' or interest_packet == 'radar/members/getTotalPeople':
            print('Total number of people in Barrack ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/lpSensor/addSensor/*v*' or interest_packet == 'accessory/lpSensor/addSensor/*v*' or interest_packet == 'vehicle/lpSensor/addSensor/*v*' or interest_packet == 'food/lpSensor/addSensor/*v*' or interest_packet == 'radar/lpSensor/addSensor/*v*':
            print('Sensor Add status in Barrack ', barrack_type[0], ':  ', data_packet)
        elif interest_packet == 'weapon/lpSensor/removeSensor/*v*' or interest_packet == 'accessory/lpSensor/removeSensor/*v*' or interest_packet == 'vehicle/lpSensor/removeSensor/*v*' or interest_packet == 'food/lpSensor/removeSensor/*v*' or interest_packet == 'radar/lpSensor/removeSensor/*v*':
            print('Sensor Remove status', barrack_type[0], ':  ', data_packet)
        elif interest_packet == 'weapon/lpSensor/boxOpen/*v*' or interest_packet == 'accessory/lpSensor/boxOpen/*v*' or interest_packet == 'vehicle/lpSensor/boxOpen/*v*' or interest_packet == 'food/lpSensor/boxOpen/*v*' or interest_packet == 'radar/lpSensor/boxOpen/*v*':
            print('Opening of box in Barrack ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/lpSensor/checkBox/*v*' or interest_packet == 'accessory/lpSensor/checkBox/*v*' or interest_packet == 'vehicle/lpSensor/checkBox/*v*' or interest_packet == 'food/lpSensor/checkBox/*v*' or interest_packet == 'radar/lpSensor/checkBox/*v*':
            print('Box Status in Barrack ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/motionSensor/addCamera/*v*' or interest_packet == 'accessory/motionSensor/addCamera/*v*' or interest_packet == 'vehicle/motionSensor/addCamera/*v*' or interest_packet == 'food/motionSensor/addCamera/*v*' or interest_packet == 'radar/motionSensor/addCamera/*v*':
            print('Camera Add update in Barrack ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/motionSensor/removeCamera/*v*' or interest_packet == 'accessory/motionSensor/removeCamera/*v*' or interest_packet == 'vehicle/motionSensor/removeCamera/*v*' or interest_packet == 'food/motionSensor/removeCamera/*v*' or interest_packet == 'radar/motionSensor/removeCamera/*v*':
            print('Camera Remove update in Barrack ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/motionSensor/checkCamera/*v*' or interest_packet == 'accessory/motionSensor/checkCamera/*v*' or interest_packet == 'vehicle/motionSensor/checkCamera/*v*' or interest_packet == 'food/motionSensor/checkCamera/*v*' or interest_packet == 'radar/motionSensor/checkCamera/*v*':
            print(' Accessing Camera in Barrack ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/vibrationSensor/addSensor/*v*' or interest_packet == 'accessory/vibrationSensor/addSensor/*v*' or interest_packet == 'vehicle/vibrationSensor/addSensor/*v*' or interest_packet == 'food/vibrationSensor/addSensor/*v*' or interest_packet == 'radar/vibrationSensor/addSensor/*v*':
            print('Vibration Sensor Add update in Barrack ',barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/vibrationSensor/removeSensor/*v*' or interest_packet == 'accessory/vibrationSensor/removeSensor/*v*' or interest_packet == 'vehicle/vibrationSensor/removeSensor/*v*' or interest_packet == 'food/vibrationSensor/removeSensor/*v*' or interest_packet == 'radar/vibrationSensor/removeSensor/*v*':
            print('Vibration Sensor Remove update in Barrack ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/vibrationSensor/checkVibrationSensor/*v*' or interest_packet == 'accessory/vibrationSensor/checkVibrationSensor/*v*' or interest_packet == 'vehicle/vibrationSensor/checkVibrationSensor/*v*' or interest_packet == 'food/vibrationSensor/checkVibrationSensor/*v*' or interest_packet == 'radar/vibrationSensor/checkVibrationSensor/*v*':
            print(' Vibration Sensor status in Barrack ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/soundSensor/addSensor/*v*' or interest_packet == 'accessory/soundSensor/addSensor/*v*' or interest_packet == 'vehicle/soundSensor/addSensor/*v*' or interest_packet == 'food/soundSensor/addSensor/*v*' or interest_packet == 'radar/soundSensor/addSensor/*v*':
            print(' Sound Sensor Add Update in Barrack ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/soundSensor/removeSensor/*v*' or interest_packet == 'accessory/soundSensor/removeSensor/*v*' or interest_packet == 'vehicle/soundSensor/removeSensor/*v*' or interest_packet == 'food/soundSensor/removeSensor/*v*' or interest_packet == 'radar/soundSensor/removeSensor/*v*':
            print(' Sound Sensor Remove Update in Barrack ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/soundSensor/getSensor/*v*' or interest_packet == 'accessory/soundSensor/getSensor/*v*' or interest_packet == 'vehicle/soundSensor/getSensor/*v*' or interest_packet == 'food/soundSensor/getSensor/*v*' or interest_packet == 'radar/soundSensor/getSensor/*v*':
            print(' Sound Status in Barrack ', barrack_type[0], ': ', data_packet)
        elif interest_packet == 'weapon/weapons/getRifles':
            print(' Rifles available: ', data_packet)
        elif interest_packet == 'weapon/weapons/getPistols':
            print('Pistols available: ',data_packet)
        elif interest_packet == 'weapon/weapons/addRifle/*v*':
            print('Rifle Added: ', data_packet)
        elif interest_packet == 'weapon/weapons/addPistol/*v*':
            print('Pistol Added: ', data_packet)
        elif interest_packet == 'weapon/weapons/removeRifle/*v*':
            print('Rifle Removed: ', data_packet)
        elif interest_packet == 'weapon/weapons/removePistol/*v*':
            print('Pistol Removed: ', data_packet)
        elif interest_packet == 'accessory/accessories/getAccessories':
            print('Accessories :', data_packet)
        elif interest_packet == 'accessory/accessories/addAccessory/*v*':
            print('Accessories add update :', data_packet)
        elif interest_packet == 'accessory/accessories/removeAccessory/*v*':
            print('Accessories remove update :', data_packet)
        elif interest_packet == 'vehicle/vehicles/getCar' or interest_packet == 'vehicle/vehicles/getTruck' or interest_packet == 'vehicle/vehicles/getArmored':
            print('Vehicles available ', data_packet)
        elif interest_packet == 'vehicle/vehicles/addCar/*v*' or interest_packet == 'vehicle/vehicles/addTruck/*v*' or interest_packet == 'vehicle/vehicles/addArmored/*v*':
            print('Vehicle add update ', data_packet)
        elif interest_packet == 'vehicle/vehicles/removeCar/*v*' or interest_packet == 'vehicle/vehicles/removeTruck/*v*' or interest_packet == 'vehicle/vehicles/removeArmored/*v*':
            print('Vehicle remove update ', data_packet)
        elif interest_packet == 'food/food/getFood':
            print('Food available :', data_packet)
        elif interest_packet == 'food/food/addFood/*v*':
            print('Food Add available :', data_packet)
        elif interest_packet == 'food/food/removeFood':
            print('Food Remove available :', data_packet)
        elif interest_packet == 'radar/radar/getradarstate':
            print('Radar State :', data_packet)

    #Sends interest package
    def sendInterest(self,interest):
        routers = {(ROUTER_IP, ROUTER_PORT)}
        print('attempting to send interest packet: ', interest)

        for router in routers:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(router)
                base64encoded = str(self.bencode(interest))
                s.send(base64encoded.encode())
                ack = s.recv(1024)
                self.actuate(interest, self.bdecode(ack.decode('utf-8')))
                s.close()
            except Exception:
                print("An exception occured")

    #Contains or the data required for the sensors' functions
    def main(self):
        weapons_interest_packets = ['weapon/co2/getGas', 'weapon/co2/getStatus',
    'weapon/temp/getStatus','weapon/temp/adjustTemp/*v*','weapon/temp/getCurrentTemp','weapon/temp/getProjectedTemp',
    'weapon/members/checkIn/*v*','weapon/members/checkOut/*v*','weapon/members/getCivillianCount','weapon/members/getMilitaryCount', 'weapon/members/getTotalPeople',
    'weapon/lpSensor/addSensor/*v*','weapon/lpSensor/boxOpen/*v*','weapon/lpSensor/checkBox/*v*','weapon/lpSensor/removeSensor/*v*',
    'weapon/motionSensor/addCamera/*v*','weapon/motionSensor/removeCamera/*v*','weapon/motionSensor/checkCamera/*v*',
    'weapon/vibrationSensor/addSensor/*v*','weapon/vibrationSensor/checkVibrationSensor/*v*','weapon/vibrationSensor/removeSensor/*v*',
    'weapon/soundSensor/addSensor/*v*','weapon/soundSensor/getSensor/*v*','weapon/soundSensor/removeSensor/*v*',
    'weapon/weapons/getRifles','weapon/weapons/getPistols', 'weapon/weapons/addRifle/*v*','weapon/weapons/addPistol/*v*','weapon/weapons/removeRifle/*v*', 'weapon/weapons/removePistol/*v*']
        accessory_interest_packets = ['accessory/co2/getGas', 'accessory/co2/getStatus',
    'accessory/temp/getStatus', 'accessory/temp/adjustTemp/*v*', 'accessory/temp/getCurrentTemp', 'accessory/temp/getProjectedTemp',
    'accessory/members/checkIn/*v*', 'accessory/members/checkOut/*v*', 'accessory/members/getCivillianCount', 'accessory/members/getMilitaryCount', 'accessory/members/getTotalPeople',
    'accessory/lpSensor/addSensor/*v*', 'accessory/lpSensor/boxOpen/*v*', 'accessory/lpSensor/checkBox/*v*', 'accessory/lpSensor/removeSensor/*v*',
    'accessory/motionSensor/addCamera/*v*', 'accessory/motionSensor/removeCamera/*v*', 'accessory/motionSensor/checkCamera/*v*',
    'accessory/vibrationSensor/addSensor/*v*', 'accessory/vibrationSensor/checkVibrationSensor/*v*', 'accessory/vibrationSensor/removeSensor/*v*',
    'accessory/soundSensor/addSensor/*v*', 'accessory/soundSensor/getSensor/*v*', 'accessory/soundSensor/removeSensor/*v*',
    'accessory/accessories/getAccessories', 'accessory/accessories/addAccessory/*v*', 'accessory/accessories/removeAccessory/*v*']
        vehicle_interest_packets = ['vehicle/co2/getGas', 'vehicle/co2/getStatus',
         'vehicle/temp/getStatus', 'vehicle/temp/adjustTemp/*v*', 'vehicle/temp/getCurrentTemp', 'vehicle/temp/getProjectedTemp',
        'vehicle/members/checkIn/*v*', 'vehicle/members/checkOut/*v*', 'vehicle/members/getCivillianCount', 'vehicle/members/getMilitaryCount', 'vehicle/members/getTotalPeople',
         'vehicle/lpSensor/addSensor/*v*', 'vehicle/lpSensor/boxOpen/*v*', 'vehicle/lpSensor/checkBox/*v*', 'vehicle/lpSensor/removeSensor/*v*',
         'vehicle/motionSensor/addCamera/*v*', 'vehicle/motionSensor/removeCamera/*v*', 'vehicle/motionSensor/checkCamera/*v*',
         'vehicle/vibrationSensor/addSensor/*v*', 'vehicle/vibrationSensor/checkVibrationSensor/*v*', 'vehicle/vibrationSensor/removeSensor/*v*',
         'vehicle/soundSensor/addSensor/*v*', 'vehicle/soundSensor/getSensor/*v*', 'vehicle/soundSensor/removeSensor/*v*',
         'vehicle/vehicles/getCar', 'vehicle/vehicles/addCar/*v*', 'vehicle/vehicles/removeCar/*v*', 'vehicle/vehicles/getTruck', 'vehicle/vehicles/addTruck/*v*', 'vehicle/vehicles/removeTruck/*v*',
         'vehicle/vehicles/getArmored', 'vehicle/vehicles/addArmored/*v*', 'vehicle/vehicles/removeArmored/*v*']
        food_interest_packets = ['food/co2/getGas', 'food/co2/getStatus',
    'food/temp/getStatus', 'food/temp/adjustTemp/*v*', 'food/temp/getCurrentTemp', 'food/temp/getProjectedTemp',
     'food/members/checkIn/*v*', 'food/members/checkOut/*v*', 'food/members/getCivillianCount', 'food/members/getMilitaryCount', 'food/members/getTotalPeople',
     'food/lpSensor/addSensor/*v*', 'food/lpSensor/boxOpen/*v*', 'food/lpSensor/checkBox/*v*', 'food/lpSensor/removeSensor/*v*',
     'food/motionSensor/addCamera/*v*', 'food/motionSensor/removeCamera/*v*', 'food/motionSensor/checkCamera/*v*',
     'food/vibrationSensor/addSensor/*v*', 'food/vibrationSensor/checkVibrationSensor/*v*', 'food/vibrationSensor/removeSensor/*v*',
     'food/soundSensor/addSensor/*v*', 'food/soundSensor/getSensor/*v*', 'food/soundSensor/removeSensor/*v*',
    'food/food/getFood', 'food/food/removeFood', 'food/food/addFood/*v*']
        radar_interest_packets = ['radar/co2/getGas', 'radar/co2/getStatus',
    'radar/temp/getStatus', 'radar/temp/adjustTemp/*v*', 'radar/temp/getCurrentTemp', 'radar/temp/getProjectedTemp',
    'radar/members/checkIn/*v*', 'radar/members/checkOut/*v*', 'radar/members/getCivillianCount', 'radar/members/getMilitaryCount', 'radar/members/getTotalPeople',
    'radar/lpSensor/addSensor/*v*', 'radar/lpSensor/boxOpen/*v*', 'radar/lpSensor/checkBox/*v*', 'radar/lpSensor/removeSensor/*v*',
    'radar/motionSensor/addCamera/*v*', 'radar/motionSensor/removeCamera/*v*', 'radar/motionSensor/checkCamera/*v*',
    'radar/vibrationSensor/addSensor/*v*', 'radar/vibrationSensor/checkVibrationSensor/*v*', 'radar/vibrationSensor/removeSensor/*v*',
    'radar/soundSensor/addSensor/*v*', 'radar/soundSensor/getSensor/*v*', 'radar/soundSensor/removeSensor/*v*',
    'radar/radar/getradarstate']
        #Guidlines for user to follow
        while True:
            print('\n')
            print('Press 1 to send  weapons interest packets')
            print('Press 2 to send  accessory interest packets')
            print('Press 3 to send  vehicle interest packets')
            print('Press 4 to send  food interest packets')
            print('Press 5 to send  radar interest packets')
            val = input()

            #If statements for correct rection of the system depending on the number selected
            if val == '1':
                for c in weapons_interest_packets:
                    print('press 1 to send next packet, press 2 to change Barrack type')
                    inp = input()
                    if inp != '1':
                        break
                    self.sendInterest(c)
                    print('\n')
            elif val == '2':
                for c in accessory_interest_packets:
                    print('press 1 to send next packet, press 2 to change Barrack type')
                    inp = input()
                    if inp != '1':
                        break
                    self.sendInterest(c)
                    print('\n')
            elif val == '3':
                for c in vehicle_interest_packets:
                    print('press 1 to send next packet, press 2 to change Barrack type')
                    inp = input()
                    if inp != '1':
                        break
                    self.sendInterest(c)
                    print('\n')
            elif val == '4':
                for c in food_interest_packets:
                    print('press 1 to send next packet, press 2 to change Barrack type')
                    inp = input()
                    if inp != '1':
                        break
                    self.sendInterest(c)
                    print('\n')
            elif val == '5':
                for c in radar_interest_packets:
                    print('press 1 to send next packet, press 2 to change Barrack type')
                    inp = input()
                    if inp != '1':
                        break
                    self.sendInterest(c)
                    print('\n')


if __name__ == '__main__':
    sendint = SendInterest()
    sendint.main()
