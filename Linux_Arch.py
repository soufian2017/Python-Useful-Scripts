#!/usr/bin/env python3

from os import system

TMP = "/tmp/test/"
FILE_NAME = "a.txt"

system("mkdir "+TMP)

system("cat /etc/os-release | grep ID > "+TMP+FILE_NAME)

with open(TMP+FILE_NAME, "r") as f:
	file = f.read()
	if "debian" in file:
		print("Debian")
	elif "arch" in file:
		print("Arch")
	elif "rhel" in file:
		print("RHEL")
	else:
		print("ERROR")
		
system("rm "+TMP+FILE_NAME) # just in case of errors.
system("rm -r "+TMP)
