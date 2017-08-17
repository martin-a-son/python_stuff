#!C:\etc\Python27\python.EXE

# Little exercise with Scriptoptions

import sys
import getopt

myAuthHash = 'some567hash234='

def usage():
    print ('Usage:')
    print ('python ' + sys.argv[0] + ' [-i|--ip <Destination IP>] [-a|--auth <Authentication Hash>] [-h|--help] [-d| --debug]')

def main(argv):
	# Variables
	global _debug
	auth = myAuthHash
	ip = '127.0.0.1'
	_debug = False
	
	# Define and get script arguments
	# Options that require an argument need to be followed by a colon.
	# I our case we want the options "-h -a <arg1> -i <arg2> -d". That means our option list is "ha:i:d".
	try:
		opts, args = getopt.getopt(sys.argv[1:], "ha:i:d", ["help", "auth=", "ip=", "debug"])
	except getopt.GetoptError as err:
		print (err)	# Will print something like "option not recognized".
		usage()
		sys.exit(2)
	
	# Go through the options and pick up their arguments.
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-d", "--debug"):
			_debug = 1
		elif opt in ("-a", "--auth"):
			auth = arg
		elif opt in ("-i", "--ip"):
			ip = arg
		else:
			assert False, "unhandled option"

	# Ignore any unwanted arguments.
	if args:
		print ('\n***Further arguments ' + str(args) + ' are ignored.***\n')

	if _debug:
		print ('myAuthHash default = ' + myAuthHash)
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
