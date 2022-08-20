#!/usr/bin/python3.8

from scapy.contrib.gtp import GTP_U_Header
from scapy.contrib.gtp import GTPEchoRequest
from scapy.all import *

sendp(Ether()/IP(src="192.168.60.154", dst="192.168.60.176")/UDP(sport=2152,dport=2152)/GTP_U_Header(S=1,gtp_type=1,seq=1)/GTPEchoRequest(),iface="enp0s8")
