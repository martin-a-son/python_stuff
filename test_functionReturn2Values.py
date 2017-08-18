# Call script like below:
# c:\> python test_functionReturn2Values.py one two
# argv = ['one', 'two']
# Wert 1 = value_one
# Wert 2 = value_two
# Kombi = onetwo

import sys

def myfunc(strA, strB):
	x = 'value_' + strA
	y = 'value_' + strB
	z = strA + strB
	return x, y, z
	
def main(argv):
	print ('argv = ' + str(argv))

	Wert_1, Wert_2, Kombi = myfunc(argv[0], argv[1])
	
	print ('Wert 1 = ' + Wert_1)
	print ('Wert 2 = ' + Wert_2)
	print ('Kombi = ' + Kombi)

if __name__ == "__main__":
    main(sys.argv[1:])
