out = ""
with open("23.perl") as f:
	blob = f.read()
	for char in blob:
		if (64 < ord(char) <= (64+26)) or (96 < ord(char) <= (96+26)):
			out += char
print(out)
