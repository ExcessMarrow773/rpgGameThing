import generation
import colorama
g = generation.generation()
g.reset()

data = {'roomName': 'Bedroom', 'description': 'A Simple Bedroom with a bed, a desk, and some chairs.'}

g.makeRoom('bedroom', data)

rooms = ['bedroom', 'bathroom', 'Kitchen', 'BAthRoom', 'living room']
i = rooms[2]
g.makeRoom(i, {'roomName': i, 'description': 'A test room built to break my engine!'})
