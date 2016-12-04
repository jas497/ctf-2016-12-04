import re

blob='''
Hi good dear,

I have some exciting info about the jail. They recently added a great workout device within their good fitness area. Very fun fitness devices will allow their very varied crew in here to hit nice fitness goals.

If I have your goals? No, you shouldn't have goals of less abs. That be scarcely make any sense.

Bye!
'''

def getpar(word):
	par = 0
	for char in word.upper():
		par += ord(char) > 77
	return par % 2

fin=[]
for word in blob.split():
	par = getpar( re.search('(\w+)', word).group(1) )
	fin.append(par)

def bit2word(bits):
	out = 0
	for bit in bits:
		out = (out << 1) | bit
	return out

print(len(fin), fin)

for i in range(0, len(fin), 5):
	sub = fin[i:i+5]
	print(chr(65 + bit2word(sub)))

flag = ""
i = 0
while i < len(fin):
	flag += chr(bit2word(fin[i:i+8]))
	i += 8

print(flag)

