import socket
import ipaddress  # This is the module, do not overwrite it
import pyfiglet
from time import sleep

# Banner
banner = "PORT SCANNER V1.0"
ascii_banner = pyfiglet.figlet_format(banner)
print(ascii_banner)

# Input
user_input = input("Enter IP address or hostname to scan: ")

# Optional: validate IP format (just to inform the user)
try:
    ipaddress.ip_address(user_input)
    print("Valid IP address format.")
except ValueError:
    print("Input is not a direct IP address, attempting to resolve hostname...")

# Resolve hostname to IP
try:
    target_ip = socket.gethostbyname(user_input)
    print(f"Resolved Target IP: {target_ip}")
except socket.gaierror:
    print("❌ Error: Invalid IP address or hostname.")
    exit()

# Simulated scanning delay
print("\nScanning", target_ip, "from port 1 to 100...\n")
for _ in range(3):
    print("...")
    sleep(1)

for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target_ip, port))
    if result == 0:
        print(f">>>>>>>>>>>Port {port} is open<<<<<<<<<<<")
    s.close()