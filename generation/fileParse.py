#import os
#import sys
#import random
import parse

class roomFiles:
	def __init__(self, roomFile):
		f = open(roomFile, 'r')
		self.fileContents = f.read()
		f.close()

	def parseRoom(self):
		return parse.parse(self.fileContents, '\n')

	def temp(self)

if __name__ == '__main__':
	file = roomFiles("roomTree.txt")
	print(file.fileContents)
	print(file.parseRoom())
