import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []

for onePort in ports:
    portsList.append(str(onePort))

val = input("Select Arduino Port: ")

for x in range(0, len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

while True:
    # TODO: audioPeriod = 
    serialInst.write(command.encode('utf-8'))

     