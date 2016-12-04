#!/usr/bin/env python3
from functools import reduce
from base64 import * 


def sweet_hash(string):
    x = 42
    byte = []

    for char in string:
        byte.append(x ^ ord(char))
        x ^= ord(char)

    return b64encode(bytes(byte))

out = b'TCBBJl06WylQfRRzHXwIYRRnSj5bOlg3UypX'
raw = b64decode(out)

def unhash(h):
	x = 42
	out = []
	for nchar in h:
		x ^= ord(nchar)
		out.append(x ^ ord(nchar))
	return [chr(x) for x in out]

print(unhash(raw))
