#!/usr/bin/env python
import socket as sock
import struct
import fcntl
import sys
import os

ifnames = os.listdir('/sys/class/net')
s = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)

fileno = s.fileno()
loopback = '127.0.0.1'


def get_available_ips():
	ips = []
	for ifname in ifnames:
		try:
			ips.append(
				sock.inet_ntoa(
					fcntl.ioctl(
						fileno, 0x8915,
						struct.pack('256s', ifname[:15]))[20:24]
					)
				)
		except:
			pass

	ips.remove(loopback)
	return ips


def on_network():
	ips = get_available_ips()
	if len(ips) > 0:
		return True
	else:
		return False


def main():
	ips = get_available_ips()
	if len(ips) > 0:
		print('true')
		sys.exit(0)
	else:
		sys.exit(1)


if __name__ == '__main__':
	main()
