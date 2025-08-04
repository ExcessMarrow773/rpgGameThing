#from battle import Battle
import colorama
from player import Player
from ui import UI
import items
#import time

UI = UI()
PLAYER = Player(name='Atticus')
player = PLAYER.createPlayer({'maxHp': 100})
UI.UI(player)

def p(input):
	UI.UI(player, input)

commands = ['exit', 'UI', 'showInvintory', 'takeItem', 'history', 'help']
help = {'exit': 'Exits the game', 'UI': 'Shows the UI', 'takeItem': 'Takes items from a container', 'showInvintory': 'Shows the invintory', 'history': 'Shows the command history', 'help': 'Shows this help message'}
history = []

while True:
	i = input("> ").strip()
	data = i.split(' ')
	history.append(i)

	match data[0]:
		case 'exit':
			UI.clear()
			break
		case 'UI':
			UI.UI(player)
		case 'takeItem':
			p(PLAYER.takeItem(items.searchItems(i[9:])))
		case 'showInvintory':
			UI.UI(player, PLAYER.showInvintory())
		case 'help':
			tmp = ''
			for i in commands:
				tmp +=(f'{i}: {help[i]}\n')
			p(tmp)
		case 'history':
			p(history)
		case _:
			p(colorama.Fore.RED+'Please try again with a valid command'+colorama.Fore.RESET)
