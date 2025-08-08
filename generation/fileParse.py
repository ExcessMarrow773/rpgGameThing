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

	def temp(self):
		words = []
		tmp = ""
		for i in range(len(self.fileContents)):
			if self.fileContents[i] == '/':
				words.append(tmp)
				tmp = ""
			elif self.fileContents[i] != "\n":
				tmp += self.fileContents[i]
		print(words)

if __name__ == '__main__':
	file = roomFiles("roomTree.txt")
	print(file.fileContents)
	print(file.parseRoom())
	file.temp()
