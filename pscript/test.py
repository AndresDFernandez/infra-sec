import nmap

def main():
    # key

    # Get IP addresses to test
    n = nmap.PortScanner()
    res = n.scan("172.16.0.11", "22")
    op = []
    for i in res["scan"]:
        if res["scan"][i]["tcp"][22]["state"] == "open":
            op.append(i)

