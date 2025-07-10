import socket

def banner(ip, port):
  try:
    with socket.socket() as s:
      s.settimeout(5)
      s.connect((ip, int(port)))
      response = s.recv(1024)
      print(f"Banner from {ip}:{port}:\n{response.decode(errors='replace')}")
  except socket.timeout:
    print(f"Connection to {ip}:{port} timed out.")
  except ConnectionRefusedError:
    print(f"Connection to {ip}:{port} was refused.")
  except Exception as e:
    print(f"An error occurred: {e}")

def main():
  try:
    ip = input("Enter the IP address: ").strip()
    port = input("Enter the port: ").strip()
    if not ip or not port.isdigit():
      print("Invalid IP address or port.")
      return
    banner(ip, port)
  except KeyboardInterrupt:
    print("\nOperation cancelled by user.")

if __name__ == "__main__":
  main()
