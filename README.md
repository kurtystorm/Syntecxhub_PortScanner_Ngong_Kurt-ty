# Syntecxhub Port Scanner

A multi-threaded TCP port scanner written in Python as part of the Syntecxhub Internship Program.

This tool scans a target host for open ports, detects service banners, and logs results automatically. It demonstrates socket programming, concurrency, exception handling, and basic service version detection.

---

## Features

- Scan a single host
- Scan custom port ranges
- Multi-threaded scanning for speed
- Detect open/closed/timeout ports
- Basic service banner grabbing
- Automatic logging of scan results
- Error handling for unreachable hosts
- Lightweight and runs on Linux/Windows

---

## Requirements

- Python 3.8+
- Linux / Windows / macOS
- No external libraries required

Check Python version:

```bash
python3 --version
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/kurtystorm/Syntecxhub_PortScanner_Ngong_Kurt-ty.git
cd Syntecxhub_PortScanner_Ngong_Kurt-ty
```

---

## Usage

Run the scanner:

```bash
python3 port_scanner.py
```

Example:

```bash
Enter target host: scanme.nmap.org
Enter start port: 1
Enter end port: 100
```

Output will show:

- Open ports
- Service banners (if available)
- Scan progress
- Logged results

---

## Log File

Each scan updates:

```
scan_log.txt
```

The log file records:

- Timestamp
- Target host
- Open ports
- Service information

---

## Project Structure

```
Syntecxhub_PortScanner/
│
├── port_scanner.py
├── scan_log.txt
└── README.md
```

---

## Learning Objectives

This project demonstrates:

- Python socket programming
- Multi-threading
- Network scanning fundamentals
- Service detection techniques
- File logging
- Exception handling
- CLI interaction

---

## Disclaimer

This tool is for **educational purposes only**.

Do not scan systems without permission. Unauthorized scanning may be illegal.

---

## Author

Ngong Kwa Wolfgang Kurt-Ty  
Cybersecurity & Network Administration

Syntecxhub Internship Project
