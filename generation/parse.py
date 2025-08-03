import os

def parse(input, parseBy):
	return input.split(parseBy)

def snake(input, replace=' '):
	output = ''
	for i in range(len(input)):
		if input[i] == replace:
			output += '_'
		else:
			output += input[i]

	return output

def roomSyntax(input):
	input = input.lower()
	output = snake(input)
	return output

if __name__ == '__main__':
	print(parse('test+1+2+3', '+'))
	print(snake('living Room'))
	print(snake('test+this+out', '+'))