from smbus2 import SMBus

LM75_ADDRESS		 = 0x48

LM75_TEMP_REGISTER 	 = 0x00

class LM75(object):
	def __init__(self, busnum=1):
		self._address = 0x48
		self._temp_register = 0x00
		self._bus = SMBus(busnum)

	def getTemp(self):
		raw = self._bus.read_word_data(self._address, self._temp_register) & 0xFFFF
		raw = ((raw << 8) & 0xFF00) + (raw >> 8)
		return raw /256

        
