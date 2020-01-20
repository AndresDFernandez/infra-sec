import socket
import ipcalc
import nmap

print('amazing super scan')

nmap = nmap.PortScanner() 
host = 
nmap.scan(host, '1-443') 

for host in nmap.all_hosts(): 
    print('Host : %s (%s)' % (host, nmap[host].hostname())) 
    print('State : %s' % nmap[host].state()) 

    # print('Host :' + nm[str(host)].hostname())
   #  print('State : %s' % nm[str(host)].state())
    for proto in nmap[str(host)].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        lport = nmap[str(host)][proto].keys()
        lport.sort()
        for port in lport:
            print ('port : %s\tstate : %s' % (port, nmap[str(host)][proto][port]['state']))    





  
