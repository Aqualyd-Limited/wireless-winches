import time
import xbee

while True:
   try:
       xbee.transmit(xbee.ADDR_BROADCAST, 'TEST')
       print('data sent')
   except Exception as e:
       print('Error occurred: {}'.format(e))

   time.sleep_ms(2000)
