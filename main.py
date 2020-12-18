from scapy import *
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp

IpScan = '192.168.*.*'
try:
    ans, unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF") / ARP(pdst=IpScan), timeout=2)
except Exception as e:
    print(e)
else:
    for send, rcv in ans:
        ListMACAddr = rcv.sprintf("%Ether.src%---%ARP.psrc%")
        print(ListMACAddr)
