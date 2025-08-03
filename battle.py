import random

class Battle:
	def __init__(self, seed=random.randrange(100000)):
		random.seed(seed)

	def startFight(self, player, enimey):
		print(enimey.name, "attacks", player.name)
