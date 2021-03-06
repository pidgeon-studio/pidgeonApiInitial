import serial
import time

class TextMessage:
  def __init__(self, recipient, message):
    self.recipient = recipient
    self.content = message

  def setRecipient(self, number):
    self.recipient = number

  def setContent(self, message):
    self.content = message

  def connectPhone(self):
    self.ser = serial.Serial('/dev/ttyUSB0', 460800, timeout=5)
    print self.ser
    time.sleep(1)

  def sendMessage(self):
    self.ser.write('AT\r')
    time.sleep(1)
    self.ser.write('AT+CSCA="+40744946000",145\r')
    time.sleep(1)
    self.ser.write('AT+CMGF=1\r')
    time.sleep(1)
    self.ser.write('''AT+CMGS="''' + self.recipient + '''"\r''')
    time.sleep(1)
    self.ser.write(self.content + "\r")
    time.sleep(1)
    self.ser.write(chr(26))
    time.sleep(1)

  def disconnectPhone(self):
    self.ser.close()
  
  def run(self):
    self.connectPhone()
    self.sendMessage()
    self.disconnectPhone()
