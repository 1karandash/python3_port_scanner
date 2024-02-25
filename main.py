import socket
import queue
import threading


target = "127.0.0.1"
open_ports = []

q = queue.Queue()

def portScan(port):
	global target
	
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((target, port))
		
		return True
	except:
		return False
		

def getPorts(mode):
	global q
	
	if mode == 1:
		for port in range (1, 1025):
			q.put(port)
	elif mode == 2:
		for port in range (1, 65536):
			q.put(port)
	elif mode == 3: 
		ports = [20, 21, 22, 23, 25, 53, 69, 80, 110, 137, 139, 443, 445, 1336, 8080, 8443, 9000]
		for port in ports:
			q.put(port)
	elif mode == 4:
		ports = input("Enter your ports separated by commas: ")
		ports = ports.split(",")
		ports = list(map(int, ports))
		for port in ports:
			if port <= 65536:
				q.put(port)
			else:
				print("Port {} is not in the ports range (1 - 65535)".format(port))

	
def worker():
	global open_ports, q

	while not q.empty():
		port = q.get()
		if portScan(port):
			print("Port {} is open!".format(port))
			open_ports.append(port)
		else:
			print("Port {} is closed!".format(port))
			
			
def runScanner():
	global open_ports
	
	print("Hi and welcome!")
	print("=========================================")
	print("The port scanner has the following modes: ")
	print("=========================================")
	print("\n")
	print("1 - For scanning the ports from 1 to 1024")
	print("2 - For scanning the well known ports like: 20, 21, 22, 80, 443 and more")
	print("3 - For scanning all the 65535 ports")
	print("4 - For manually chosing which port(s) to scan")
	print("\n")
	input("Press Enter to continue...")

	mode = int(input("Please choose the mode (1-4): "))
	threads = int(input("Please set the number of threads: "))
	
	getPorts(mode)
	
	thread_list = []
	
	for t in range(threads):
		thread = threading.Thread(target=worker)
		thread_list.append(thread)

	for thread in thread_list:
		thread.start()
		thread.join()
		
	print("Open ports are: ", open_ports)


runScanner()
