import socket
import threading
from queue import Queue

target = "localhost" # Change this to the target IP or hostname
queue = Queue()
open_ports = []

def scan_port(port):
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    sock.connect((target, port))
    sock.close()
    return True
  except (socket.timeout, ConnectionRefusedError, OSError):
    return False

for port in range(1, 1024):
  if scan_port(port):
    print(f"Port {port} is open on {target}")
  else:
    print(f"Port {port} is closed on {target}")
    
def fill_queue():
  for port in range(1, 1024):
    queue.put(port)

def worker():
  while not queue.empty():
    port = queue.get()
    if scan_port(port):
      open_ports.append(port)
      print(f"Port {port} is open on {target}")
    queue.task_done()
    
port_list = list(range(1, 1024))
fill_queue()

thread_list = []

for t in range (100):
  thread = threading.Thread(target=worker)
  thread_list.append(thread)
  
for thread in thread_list:
  thread.start()
  
for thread in thread_list:
  thread.join() 
  
print(f"Open ports: {open_ports}")
print("Port scanning completed.")
print("All threads have finished execution.")
print("Exiting the program.")
print("Thank you for using the port scanner.")
print("Goodbye!")
