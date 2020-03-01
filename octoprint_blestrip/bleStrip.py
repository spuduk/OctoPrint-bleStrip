###################################
##                               ##
## bleStrip controller interface ##
##                               ##
###################################
#!/usr/bin/env python

from __future__ import print_function

import binascii
import pygatt

MAC = 'BE:FF:80:00:B6:AB'
ADDRESS_TYPE = ''

UUID = '0000fff3-0000-1000-8000-00805f9b34fb'
#'7e070503ffff0000ef'
Rvalue = '00'
Gvalue = 'ff'
Bvalue = '00'
value = '7e070503'+ Rvalue+ Gvalue+ Bvalue+ '00ef'
#value2 = bytearray([0x7e, 0x07, 0x05, 0x03, 0xff, 0xff, 0x00, 0x00, 0xef])

#bavalue = bytearray(binascii.unhexlify(value))
#print (binascii.hexlify(value2))

adapter = pygatt.GATTToolBackend()
adapter.start(reset_on_start=True)
##adapter.start()

device = adapter.connect(self._settings.get(["MAC"]), timeout=30, auto_reconnect=True)

#device = adapter.connect(YOUR_DEVICE_ADDRESS, address_type=ADDRESS_TYPE)

device.char_write(UUID, bytearray([0x7e, 0x07, 0x05, 0x03, 0x00, 0x00, 0x00, 0x00, 0xef]), wait_for_response=True)
#device.disconnect()

class bleStrip:
#    def __init__(self):
#        adapter = pygatt.GATTToolBackend()
#        adapter.start(reset_on_start=True)
        #adapter.start()
#        device = adapter.connect(YOUR_DEVICE_ADDRESS, timeout=30, auto_reconnect=True)

    def ledcolor(self, rv, gv, bv):
	value = '7e070503'+ rv+ gv+ bv+ '00ef'
        device.char_write(UUID, bytearray(binascii.unhexlify(value)), wait_for_response=True)
#        device.disconnect()
