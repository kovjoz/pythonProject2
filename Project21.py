#def mysplit(strng):

def mysplit(strng):
    mylist = []
    elem = ""
    strng = strng.strip()
    counter = len(strng)
    for i in strng:
        counter -= 1
        if i != "":
            elem = elem + i
        if ord(i) == 32:
            elem = elem.rstrip()
            mylist.append(elem)
            elem = ""
        if counter == 0:
            mylist.append(elem)
    return mylist

"""
print(mysplit("Egy fa"))
print("Egy fa".split())
print(mysplit("Lenni vagy nem lenni, akkor nemesb-e a lélek ha to be or not to,be"))
print("Lenni vagy nem lenni, akkor nemesb-e a lélek ha to be or not to,be".split())
print(mysplit("To be or not to be,that is the question"))
print("To be or not to be,that is the question".split())
print(mysplit("k erkofek"))
print("k erkofek".split())
print(mysplit(" abc "))
print(" abc ".split())
print(mysplit(""))
print("".split())
"""

digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]


def print_number(num):
	global digits
	digs = str(num)
	lines = [ '' for lin in range(5) ]
	for d in digs:
		segs = [ [' ',' ',' '] for lin in range(5) ]
		ptrn = digits[ord(d) - ord('0')]
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for lin in range(5):
			lines[lin] += ''.join(segs[lin]) + ' '
	for lin in lines:
		print(lin)


print_number(int(input("Enter the number you wish to display: ")))

