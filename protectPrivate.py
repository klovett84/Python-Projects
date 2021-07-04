class ProtectPrivate:
    def __init__(self):
        self._protectedVar = True #Protecte variable
        self.__privateVar = 0 #Private variable

    #Two functions to print and change the value of privateVar
    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

#Instantiate ProtectPrivate object and print protectedVar
ProtectObj = ProtectPrivate()
print(ProtectObj._protectedVar)

#Print privateVar, change its value, and print it again
ProtectObj.getPrivate()
ProtectObj.setPrivate(42)
ProtectObj.getPrivate()
