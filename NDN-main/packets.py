#Author: Jeremie Sajeev Daniel
#This class is a small placeholder that allows for differentiating between Interest and Data packets
class InterestPacket:

    def __init__(self) -> None:
        self.header = "%INTEREST%:"
    
    def encodeData(self,x):
        return self.header + x

    def decodeData(self,x):
        return x.replace(self.header,'')

class DataPacket:

    def __init__(self) -> None:
        self.header = "%DATA%:"
    
    def encodeData(self,x):
        return self.header + x

    def decodeData(self,x):
        return x.replace(self.header,'')