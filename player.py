#import random
import items
class Player:
	def __init__(self, name=None):
		self.name = name
		self.stats = {}
		self.attacks = {}
		self.invintory = []
		self.armor = []
		self.currentHp = 0
		self.maxHp = 0
		self.level = 0
		self.data = {}

	def createPlayer(self, build, data={'username': '', 'level': 0}):
		if self.name == None:
			self.name = data['username']
		self.level = data['level']
		self.stats = build
		self.maxHp = self.stats['maxHp']
		self.currentHp = self.maxHp

		self.data={
				'username': self.name,
				'level': self.level,
				'stats': self.stats,
				'maxHp': self.maxHp,
				'currentHp': self.currentHp
			 }
		return self.data




	def takeItem(self, id):
		if items.item(id) != '':
			self.invintory.append(items.item(id))
			return f'{self.data["username"]} put {items.item(id)["name"]} in their invintory\n'
		else:
			return 'Could not find item in database, check your spelling'

	def showInvintory(self):
		output = ''
		for i in self.invintory:
			output += f'\n{i}'
		return output



	def changeData(self, data):
		self.data=data

	def hurt(self, damage):
		self.data['currentHp'] -= damage

	def regen(self, regen):
		if self.data['maxHp'] < self.data['currentHp']+regen:
			self.data['currentHp'] = self.data['maxHp']
		else:
			self.data['currentHp'] += regen
