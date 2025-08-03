import generation
import colorama

def runTests():
	g = generation.generation()
	g.reset()

	data = {'roomName': 'Bedroom', 'description': 'A Simple Bedroom with a bed, a desk, and some chairs.'}

	rooms = ['bedroom', 'bathroom', 'Kitchen', 'BAthRoom', 'living room']
	returns = []
	for i in rooms:
		print('Making room:', i)
		returns.append(g.makeRoom(i, {'roomName': i, 'description': 'A test room built to break my engine!'}))

	correctRooms = ['Created room bedroom', 'Created room bathroom', 'Created room kitchen', 'Room "bathroom" has already been created', 'Created room living_room']

	for i in range(len(rooms)):
		if correctRooms[i] == returns[i]:
			print(f'Given: "{rooms[i]}", Expected: "{correctRooms[i]}", Returned: \'{returns[i]}\' Results:', colorama.Fore.GREEN+'PASS'+colorama.Fore.RESET)
		else:
				print(f'Given: "{rooms[i]}", Expected: "{correctRooms[i]}", Returned: "{returns[i]}" Results:', colorama.Fore.RED+'FAIL'+colorama.Fore.RESET)

if __name__ == "__main__":
	runTests()
