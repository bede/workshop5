import sys

def hello(name):
	return f'Hello {name}'

def main():
	print(hello(sys.argv[1]))

if __name__ == '__main__':
	main()