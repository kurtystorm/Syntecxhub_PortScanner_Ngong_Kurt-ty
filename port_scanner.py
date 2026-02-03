import socket
from concurrent.futures import ThreadPoolExecutor
import datetime

target = input("Enter target IP or hostname: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

logfile = f"log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

def grab_banner(sock):
    try:
        sock.send(b"HELLO\r\n")
        banner = sock.recv(1024).decode().strip()
        return banner
    except:
        return "No banner detected"

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        result = s.connect_ex((target, port))

        if result == 0:
            banner = grab_banner(s)
            message = f"[OPEN] Port {port} | Service: {banner}\n"
        else:
            message = f"[CLOSED] Port {port}\n"

        print(message.strip())

        with open(logfile, "a") as f:
            f.write(message)

        s.close()

    except Exception as e:
        error_msg = f"[ERROR] Port {port}: {e}\n"
        print(error_msg.strip())
        with open(logfile, "a") as f:
            f.write(error_msg)

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(start_port, end_port + 1))

print(f"Scan complete. Results saved in {logfile}")
