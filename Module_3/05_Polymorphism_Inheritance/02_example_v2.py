class Device:
    def __init__(self, model):
        self.model = model

    def scan_vuln(self):
        raise NotImplementedError("This method should be implemented")


class Computer(Device):
    def scan_vuln(self):
        return f"[+] Updating vulnerability database for {self.model}"


class Router(Device):
    def scan_vuln(self):
        return f"[+] Multiple ports are open: Rebooting the router {self.model}"


class Smartphone(Device):
    def scan_vuln(self):
        return f"[+] {self.model} is up to date"


def scan_vulnerabilities(device):
    print(device.scan_vuln())


pc = Computer("Lenovo")
router = Router("Cisco")
smartphone = Smartphone("iPhone")


scan_vulnerabilities(pc) # [+] Updating vulnerability database for Lenovo
scan_vulnerabilities(router) # [+] Multiple ports are open: Rebooting the router Cisco
scan_vulnerabilities(smartphone) # [+] iPhone is up to date