"""
Ping the Internet!
(c) 2024 Logan Dhillon. All rights reserved.
"""
import requests
import threading
import os
import uuid
from colorama import Fore
from multiprocessing import Pool

# this value is independent for each worker, so it is just used for the log.
local_valid_http_ips = []

def log(s, fore=Fore.RESET):
    print(f"[{Fore.CYAN}Worker-{os.getpid()}{Fore.RESET}] {fore}{s}{Fore.RESET}")


pool = None
if __name__ == "__main__":
    num_workers = 12
    log(f"Registering {num_workers} workers... this may take a while if there are many workers")
    pool = Pool(processes=num_workers)


def main():
    log("Registered! Dispatching tasks to pool now", Fore.GREEN)
    pool.map(dispatch_sect_1, range(1, 256))


def dispatch_sect_2(i, j):
    log(f"Dispatching {i}.{j}.xxx.xxx scanners to worker pool")

    for k in range(1, 256):
        log(f"Scanning IP range {i}.{j}.{k}.xxx; this worker is now at {len(local_valid_http_ips)} valid IP(s).", Fore.LIGHTBLUE_EX)

        for l in range(1, 256):
            threading.Thread(
                target=lambda ip=f"{i}.{j}.{k}.{l}": check_ip(ip)).start()


def dispatch_sect_1(i):
    log(f"Dispatching {i}.xxx.xxx.xxx scanners to threads")
    for j in range(1, 256):
        threading.Thread(target=lambda: dispatch_sect_2(i, j)).start()


def check_ip(ip: str):
    try:
        response = requests.get(f"http://{ip}", timeout=2)
        if response.ok:
            local_valid_http_ips.append(ip)
            print('\a')
            with open(f"out/{uuid.uuid4()}", 'a') as f:
                f.write(ip+'\n')
            log(f"Valid IP! {ip} saved to disk.", Fore.GREEN)
    except:
        pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("Program interuptted, exiting gracefully...", Fore.YELLOW)
        pool.close()
        exit(0)
