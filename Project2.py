# Python Essentials 2

# Strings
# Python strings are immutable

# can be: + , * , += , *=
s1 = "first"
s1 += "1"
print(s1)

# ord()  for ASCII / Unicode code
print(" The ord() method  ".center(60,"*"))
s3 = "z"
print(ord(s3))
s4 = "€"
print(s4, ": ", ord(s4))

# chr()  The function takes a code point and returns its character
# chr(ord(x)) == x ,  ord(chr(x)) == x
print(" The chr() method  ".center(60,"*"))
print(chr(122))

# Strings as sequences: indexing
print(" Strings as sequences: indexing ".center(60,"*"))
s5 = "Eagle fly free"
for ix in range(len(s5)):
    print(s5[ix], end="")
print()
print(s5[-3])

# Strings as sequences: iterating
s6 = "Moonchild"
for i in s6:
    print(i, end="")
print()
# Slices  Slices    Slices  Slices
print(" The Slices method  ".center(60,"*"))
alpha = "abdefg"
"""      012345
print(alpha[1:3])   bd
print(alpha[3:])    efg
print(alpha[:3])    abd
print(alpha[3:-2])   e
print(alpha[-3:4])   e
print(alpha[::2])    adf
print(alpha[1::2])   beg  , 1-től a végéig kettes lépésközzel
"""

# The in and not in operators
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)

# min()   ASCII(A) < ASCII(a) !
# max()
print(min("aAbByYzZ"))

# index() method
s7 = "Powerslave"
print(s7.index("w"))

# list() , count()
print(list(s7))
print(s7.count("e"))

# back from list to string
print(" back from list to string  ".center(60,"*"))
li1 = list(s7)
str1 = ""
for i in li1:
    str1 += i
print("1: ", str1)
print("2: ", "".join(li1))  # back from list to string with  .join() !

# The capitalize() method
# if the first character inside the string is a letter it will be converted to upper-case;
# all remaining letters from the string will be converted to lower-case.
print(" The capitalize() method  ".center(60,"*"))
print("alphA Beta gAMMA".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

# The center() method
print("Delta".center(25,"-"))

# The startswith(), endswith() method
print(" The startswith(). endswith() method ".center(60,"*"))
t = "zeta"
print(t.endswith("a"))
print("omega".startswith("meg"))

# The find() method returns the index of first occurrence of the substring
# for a single character use "in" !
print(" The find() method  ".center(60,"*"))
print("Eta".find("ta"))
print("Eta".find("mma"))
# two-parameter variant, from any position
print('kappa'.find('a', 3))

print(" Text iteration  ".center(60,"*"))
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)

# There is also a three-parameter mutation of the find() method
print('kappa'.find('a', 1, 4))

# The isalnum() method
print(" The isalnum() method  ".center(60,"*"))
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

print(" The isalpha() method  ".center(60,"*"))
print("Moooo".isalpha())
print('Mu40'.isalpha())

print(" The isdigit() method  ".center(60,"*"))
print('2018'.isdigit())
print("Year2019".isdigit())

# The join() method
print(" The join() method  ".center(60,"*"))
print(", ".join(["omicron", "pi", "rho"]))

# upper() ,  lower()
print(" The upper(), lower() method  ".center(60,"*"))
print("SiGmA=60".lower())
print("UpperUP".upper())

# The lstrip() , rstrip(), and The strip() method - make a new string lacking the chars in the params
print(" The lstrip() , rstrip() and The strip() method ".center(60,"*"))
print("www.cisco.com".lstrip("w.c"))
print("pythoninstitute.org".lstrip("p.org"))
print("cisco.com".rstrip(".csom"))
print("pythoninstitute.org".strip("p.org"))

# The replace() method
# The two-parameter replace() method returns a copy of the original string
# in which all occurrences of the first argument have been replaced by the second argument.
print(" The replace() method  ".center(60,"*"))
print("This is it!".replace("is", "are"))
print("This is it!".replace("", "x"))
print("This is it!".replace("i", ""))
#The three-parameter replace() variant uses the third argument (a number) to limit the number of replacements.
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

# The rfind() method start their searches from the end of the string (r=right)
print(" The rfind() method  ".center(60,"*"))
print("tau tau tau".rfind("ta", 3, 9))

print("tau tau tau".rfind("ta"))
print("tau tau tau".find("ta"))

# The split() method The method assumes that the substrings are delimited by whitespaces
# The reverse operation can be performed by the join() method.
print(" The split() method  ".center(60,"*"))
print("Live wire".split())

list11 = "Li ve wir e".split()
print(list11)
print("".join(list11))

# The swapcase() method, The title() method
print(" The swapcase() method, The title() method  ".center(60,"*"))
print("I know that I know nothing 123.".swapcase())
print("I know that I know nothing. 456.".title())


# Comparing strings
#print('10' == '010')
#print('10' > '0010')
print("700099" < "811")

# Sorting  ---- ASCII(A) < ASCII(a) !!! (During sorting Capital words come first)
# Sort1:  a function named sorted(). The function takes one argument (a list) and returns a new list
print(" Sorting  ".center(60,"*"))
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

# Sort2: The sort() method affects the list itself - no new list is created.
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)

s9 = '\''
print(len(s9))

