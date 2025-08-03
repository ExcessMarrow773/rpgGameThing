import colorama, os, time

class UI:
	init = False
	def __init__(self):
		os.system('clear')
		self.titleBarUI = colorama.Back.LIGHTBLUE_EX+colorama.Fore.BLACK
		self.reset = colorama.Fore.RESET+colorama.Back.RESET
		init = True

	def startUi(self):
		tim = time.asctime()
		bar = str(tim) +(' '*(147-len(str(tim))))
		os.system("clear")
		print(self.titleBarUI+bar+self.reset)

	def middle(self):
		for i in range(17):
			print('\n')

	def box(self):
		output = '+'
		for i in range(145):
			output += '-'
		output += '+\n'
		for i in range(33):
			output += '|'+(' '*145)+'|\n'
		output += '+'
		for i in range(145):
			output += '-'
		print(output)

	def healthBar(self, player):
		hpBar = '['+(colorama.Back.BLUE+colorama.Fore.RED+'█'* round(player['currentHp']/5))+(' '*round(((player['maxHp']-player['currentHp'])/5)))+self.reset+']'
		print(hpBar)
	def clear(self):
		os.system('clear')
	def UI(self, player, middle=True):
		self.startUi()
		if middle == True:
			self.middle()
		elif not middle:
			self.box()
		else:
			index = 0
			for i in range(len(middle)):
				if middle[i] == '\n':
					index += 1
			index = 33 - index
			print(middle, ('\n'*index))
		self.healthBar(player)
