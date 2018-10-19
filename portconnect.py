#!/usr/bin/python3

import time
import socket
import re
import sys
success = 0
fail = 0
timeFactor = 5
def check_server(address, port):
	# Create a TCP socket
	s = socket.socket()
	print ("Attempting to connect to %s on port %s" % (address, port))
	try:
		s.connect((address, port))
		#print (s)
		print ("Connected to %s on port %s" % (address, port))
		return (True,s)
	except socket.error as e:
		print ("Connection to %s on port %s failed: %s" % (address, port, e))
		return (False,0)
		
def closePort(s):
	s.close()
for t in range(0,timeFactor):
	if __name__ == '__main__':
		from optparse import OptionParser
		parser = OptionParser()

		parser.add_option("-a", "--address", dest="address", default='localhost', help="ADDRESS for server", metavar="ADDRESS")
		parser.add_option("-p", "--port", dest="port", type="int", default=80, help="PORT for server", metavar="PORT")
		parser.add_option("-c", "--count", dest="count", type="int", default=50, help="COUNT for server", metavar="COUNT")
		(options, args) = parser.parse_args()
		#print ('options: %s, args: %s' % (options, args))
		for n in range(0,options.count):
			check = check_server(options.address, options.port)
			print ('check_server returned %s' % check[0])
			print ('Count = {} in Sequence {}'.format(n,t))
			if check[0] == True:
				success += 1
				closePort(check[1])
				print ('Connection Closed\n\n')
			if check[0] == False:
				fail += 1
			time.sleep(timeFactor)
		timeFactor = timeFactor - 1
	
	print ('\n\tSequence {} seconds Success = {}, Fail = {}\n\n'.format(timeFactor,success,fail))
	success = 0
	fail = 0
sys.exit(not check)

