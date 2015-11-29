#!/usr/bin/env python
import urllib2
from time import sleep

def main():
	opener = urllib2.build_opener()
	connected = False
	while not connected:
		try:
			response = opener.open( 'http://192.168.0.10/get_commandlist.cgi' ).read()
			
			#response is xml file describing endpoints (urls.cgi) we can call:
			
			if response.count('<version>2.50</version>') >0:
				connected = True
		except:
			print "Trying to connect..."
		sleep(3)
	print "Connected!"
	cmd = ''
	while cmd != 'exit':
		cmd = raw_input("Enter play/shutter/rec/off : ")
		if cmd in ['play', 'shutter', 'rec']:
			print opener.open( 'http://192.168.0.10/switch_cammode.cgi?mode=' + cmd ).read()
		if cmd == 'shutter':
			sleep(0.5)
			print opener.open( 'http://192.168.0.10/exec_shutter.cgi?com=1st2ndpush' ).read();
			sleep(0.5)
			print opener.open( 'http://192.168.0.10/exec_shutter.cgi?com=2nd1strelease' ).read();
		if cmd == 'off':
			opener.open( 'http://192.168.0.10/exec_pwoff.cgi' ).read();
	
	print 'bye'
	return 0

if __name__ == '__main__':
	main()

