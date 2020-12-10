#!/usr/bin/env python3
import argparse
import sys
import socket
import pytricia


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="file", help="File with list of domains or IP/IP-range")
    option = parser.parse_args()
    return option


BLACKLIST = [
    "190.93.240.0/20",
    "131.0.72.0/22",
    "108.162.192.0/18",
    "199.83.128.0/21",
    "198.143.32.0/19",
    "185.11.124.0/22",
    "192.230.64.0/18",
    "45.223.0.0/16",
    "172.64.0.0/13",
    "103.31.4.0/22",
    "197.234.240.0/22",
    "198.41.128.0/17",
    "104.16.0.0/12",
    "103.28.248.0/22",
    "45.64.64.0/22",
    "103.21.244.0/22",
    "103.22.200.0/22",
    "141.101.64.0/18",
    "188.114.96.0/20",
    "162.158.0.0/15",
    "149.126.72.0/21",
    "107.154.0.0/16",
    "45.60.0.0/16",
    "173.245.48.0/20",
]

BL = pytricia.PyTricia()
for i in BLACKLIST:
    BL[i] = True


def is_blacklisted(ip):
    if ip in BL:
        return True


def main():
    options = get_arguments()
    for to_check in open(options.file).readlines():
        to_check = to_check.strip()
        try:
            socket.inet_aton(to_check)
            if is_blacklisted(to_check):
                print(f"{to_check} belongs to a CDN")
            else:
                print(f"{to_check} doesn't belong to any CDN")
        except socket.error:
            to_check_ip = socket.gethostbyname(to_check)
            if is_blacklisted(to_check_ip):
                print(f"{to_check}:{to_check_ip} belongs to a CDN")
            else:
                print(f"{to_check}:{to_check_ip} doesn't belong to any CDN")

try:
    if __name__ == '__main__':
        main()
except socket.gaierror:
    print('[*] Only supply list of domains that resolve.')
except:
    print('[-] Usage: python3 filterCDN.py -f file.txt')
# NSLcrew_|_n_e_r_r_o_r_s_e_c_|
