import os
import io
import sys


def read_png():
	file_path = sys.argv[2]
	if not os.path.exists(file_path):
		print("invalid file path")
		sys.exit()
	file = open(file_path, "r", errors="ignore")
	start = False # check if the text has started
	for line in file:
		if line == "start\n":
			start = True
		if start:
			print(line)
	file.close()
	pass


def write_png():
	file1_path = sys.argv[2] # text file
	file2_path = sys.argv[3] # image file
	if not os.path.exists(file1_path) or not os.path.exists(file2_path):
		print("invalid file path")
		sys.exit()
	file1 = open(file1_path, "r")
	file2 = open(file2_path, "a")

	for line in file1:
		file2.write(line)
	pass

if sys.argv[1] != "read" and sys.argv[1] != "write":
	print("first argument isn't read or write command")
	sys.exit()
func = sys.argv[1] # variable for which function is being requested

if func == "read" and len(sys.argv) != 3:
	print("invalid number of parameters for read")
	sys.exit()
if func == "write" and len(sys.argv) != 4:
	print("invalid number of parameters for write")
	sys.exit()

if func == "write": write_png()
if func == "read": read_png()