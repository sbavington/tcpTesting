#!/usr/bin/python3

import time
import socket
import re
import array
import sys
from pbrsGen import *
success = 0
fail = 0
timeFactor = 0.02
cycles = 2
seq = randomizer_xor_sequence()


f = open('connect.log', 'w')
connectCount = 0
dataArray =[]
data =''

def check_server(address, port):
		# Create a TCP socket
		s = socket.socket()
		t = time.time()
		print ("%i %s Attempting to connect to %s on port %s" % (connectCount, t, address, port))
		#f.write ("%i %s Attempting to connect to %s on port %s " % (connectCount, t, address, port))
		try:
				s.connect((address, port))
				print ("Connected to %s on port %s" % (address, port))
				#f.write ("Connected to %s on port %s " % (address, port))
				senddata = data.encode()
				sent = s.send(data.encode('utf-8'))
				print ('Sent: {}'.format(data))
				#f.write ('\nSent: {} '.format(data))
				remaining = (len(senddata))
				result = ''
				while remaining != 0:
					got = s.recv(remaining)
					remaining = remaining - len(got)
					result = ''.join([result,got.decode()])
				print ('Got: {} '.format(result))
				#f.write ('\nGot: {} '.format(result))
				if result == data:
						print ('Returned good ')
						#f.write ('\nReturned good ')
				elif result != data:
					print ('Returned Bad ')
					f.write ("%i %s Attempting to connect to %s on port %s " % (connectCount, t, address, port))
					f.write ('\nSent: {} '.format(data))
					f.write ('\nGot: {} '.format(result))
					f.write ('\nReturned Bad ')

				return (True,s)
		except socket.error as e:
				print ("Connection to %s on port %s failed: %s" % (address, port, e))
				f.write ("Connection to %s on port %s failed: %s " % (address, port, e))
				return (False,0)

		
def closePort(s):
	s.close()
for t in range(0,cycles):
	if __name__ == '__main__':
		from optparse import OptionParser
		parser = OptionParser()
		parser.add_option("-a", "--address", dest="address", default='localhost', help="ADDRESS for server", metavar="ADDRESS")
		parser.add_option("-p", "--port", dest="port", type="int", default=80, help="PORT for server", metavar="PORT")
		parser.add_option("-c", "--count", dest="count", type="int", default=50, help="COUNT for server", metavar="COUNT")
		(options, args) = parser.parse_args()
		for n in range(0,options.count):
			for i in range(len(seq)):
				data = data +('0x%02X' % seq[i])
				connectCount += 1
				for z in range(0,8):
					check = check_server(options.address, options.port)
					print ('check_server returned %s ' % check[0])
					#f.write ('check_server returned %s \n' % check[0])
					print ('Count = {} in Sequence {} '.format(n,t))
					#f.write ('Count = {} in Sequence {} \n'.format(n,t))
					if check[0] == True:
						success += 1
						closePort(check[1])
						print ('Connection Closed\n\n')
						#f.write ('Connection Closed\n')
				if check[0] == False:
					fail += 1
				time.sleep(timeFactor)
	
	print ('\n\tSequence {} seconds Success = {}, Fail = {}\n\n'.format(t,success,fail))
	f.write ('\n\tSequence {} seconds Success = {}, Fail = {}\n\n'.format(t,success,fail))
	success = 0
	fail = 0
sys.exit(not check)
f.close()
