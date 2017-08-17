#!C:\etc\Python27\python.EXE

# Little exercise with Scriptoptions

import sys
import getopt

myAuthHash = 'some567hash234='

def usage():
    print ('Usage:')
	# print ('python myscript.py [-a|--auth <Authentication Hash>] [-h|--help] [-d]')
    print ('python ' + sys.argv[0] + ' [--ip <Destination IP>] [--auth <Authentication Hash>] [-h|--help] [-d]')
    print ('-d: debug mode')

def main(argv):
	# Variables
	global _debug
	auth = myAuthHash
	ip = '127.0.0.1'
	_debug = False
	
	# Define and get script arguments
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hai:d", ["help", "auth=", "ip="])
	except getopt.GetoptError as err:
		print (err)	# Will print something like "option not recognized".
		usage()
		sys.exit(2)
	
	# FIXME: 17.08.2017
	# Weired:
	# For some reason the options "-a" never works, "-i" sometimes works but "--ip" and "--auth" always work
	# leaving it for now
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt == '-d':
			_debug = 1
		elif opt in ("-a", "--auth"):
			auth = arg
		elif opt in ("-i", "--ip"):
			ip = arg
		else:
			assert False, "unhandled option"

	if _debug:
		print ('myAuthHash = ' + myAuthHash)
		print ('opts = ' + str(opts))
		print ('args = ' + str(args))
		if auth == "":
			print ('auth = "nix"')
		else:
			print ('auth = ' + auth)
		
		if ip == "":
			print ('ip = "nix"')
		else:
			print ('ip = ' + ip)
if __name__ == "__main__":
    main(sys.argv[1:])
