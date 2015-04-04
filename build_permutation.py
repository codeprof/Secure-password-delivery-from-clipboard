#!/usr/bin/python
import os

out = ""
org = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_#!+?$%~"
new = list(org)
rnd = list(os.urandom(1000))
for num in rnd:
	idx = ord(num) % len(org)
	new[0], new[idx] = new[idx], new[0]

for s in new:
	out = out + s

f = open ("./chromium_plugin/program.js", "r+")
data = f.read()
newdata = data.replace('5gUGZ7TavzbDRnQAxpriujPN~6?H#tKy8mf+MFc_1$XVsq9eEoBJwk%3h4SWLd0O!C2lYI', out)
if data <> newdata:
	f.seek(0)
	f.write(newdata)
	print "New permutation string generated"
	print out
else:
	print "ERROR: Failed to replace permutation string"
    
    
