import os
import random
import sys
import parse
class generation:
	def __init__(self, roomPath = 'rooms/'):
		os.system('clear')
		self.path = roomPath
		self.roomPath = roomPath
		self.tmp = None

	def openRoom(self, room):
		self.path += room
		if self.path[:1] != '/':
			self.path += '/'


	def closeRoom(self):
		print('Before:', self.path)
		if self.path != self.roomPath:
			print('got past roomPath check')
			self.tmp = self.path.split('/')
			print('tmp:', self.tmp, 'tmp len:', len(self.tmp)-1)
			self.path = ''
			for i in range(len(self.tmp)-2):
				if i == 0:
					self.path += self.tmp[i]
				else:
					self.path += '/'+self.tmp[i]
			if self.path[:1] != '/':
				self.path += '/'
		print('After:', self.path)

	def reset(self):
		os.system('rm rooms/* -rf')

	def showRooms(self, inside=False):
		if not inside:
			print(os.listdir(self.roomPath))
		return os.listdir(self.roomPath)

	def makeRoom(self, roomName, data: dict):
		roomName = parse.roomSyntax(roomName)
		if not roomName in self.showRooms(inside=True):
			print('Creating room:', roomName)
			os.system(f'mkdir {self.path}{roomName}')
			self.openRoom(roomName)
			f = open(f'{self.path}contents.txt', 'w')
			f.write(str(data))
			f.close()
			self.closeRoom()
			return f'Created room {roomName}'
		else:
			print(f'Room "{roomName}" has already been created')
			return (f'Room "{roomName}" has already been created')
