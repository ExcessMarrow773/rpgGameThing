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
		words = self.parseRoom()
		tmp = ""
		rooms = {}
		for i in range(len(words)):
			layer = 1
			for d in str(words[i]):
				if d == "-":
					layer += 1
				else:
					break
			if layer != 1:
				g = 1
				while True:
					if rooms[str(words[g][layer-1:len(words[i])-1]["layer"] == (layer-1):
						rooms[str(words[g][layer-1:len(words[i])-1]["children"][str(words[i][layer-1:len(words[i])-1])] = {"children": [], "layer": layer}
			else:
				rooms[str(words[i][layer-1:len(words[i])-1])] = {"children": [], "layer": layer}
		return rooms

rooms = {
	"kitchen": {
		"children": {
			"bathroom": {
				"children": None
				}
			}
		},
	"bedroom": {
		"children": None
		}
	}

if __name__ == '__main__':
	file = roomFiles("roomTree.txt")
	print(file.fileContents)
	print(file.parseRoom())
	print(file.temp())
	if file.temp() == rooms:
		print("\n\nIt works!")
	else:
		print("\n\nIt doesnt work :(")
