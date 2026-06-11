# Python-Scanner
A multi-threaded python scanner for fast port scanning and service Detection.
!(result.png)

# Multi-Threaded Port Scanner & Banner Grabber 

A fast, lightweight, and smart network reconnaissance tool written in Python. Developed by **x3bdulaziz** for ethical hacking and penetration testing purposes.

## Features 
* **Multi-threading Engine:** Uses `ThreadPoolExecutor` for concurrent and ultra-fast scanning.
* **Service Mapping:** Automatically identifies common network ports (SSH, HTTP, SMB, VMware, etc.).
* **Smart Banner Grabbing:** Captures raw banners and falls back to HTTP probing for silent ports.

## How It Works 
1. Validates input arguments to ensure safe runtime execution.
2. Performs a TCP handshake (`connect_ex`) asynchronously across ports 1-1000.
3. Intercepts incoming banners and cleans text formatting for actionable analysis.

## Usage 
Run the script from your terminal:
```bash
python3 scanner.py <target_ip_or_domain>
