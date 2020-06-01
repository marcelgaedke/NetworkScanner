import subprocess
import re

class NetworkScanner():

    def get_subnet(self):
        process = subprocess.Popen(['ifconfig','wlp2s0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        pattern = r'(?<=inet )(\d{3}.\d{3}.\d{3}.)(?=\d{3})'
        match = re.search(pattern, str(stdout))
        subnet = match.group(0)+'0/24'
        return subnet


    def scan(self, subnet):
        process=subprocess.Popen(['sudo', 'nmap', '-sn', '-R', subnet], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        for item in str(stdout).split('Nmap scan report for'):
            if re.search(r'Host is up', item):
                match = re.search(r'(.*)(?=Host is up)',item).group(0)
                device_name = re.search(r'.*(?= \()',match).group(0)
                device_ip = re.search(r'\d{3}.\d{3}.\d{3}.\d{3}',match).group(0)
                match2 = re.search(r'(?<=MAC Address: )(.*)',item)
                if match2:
                    match2 = match2.group(0)
                    device_mac = re.search(r'..:..:..:..:..:..',match2).group(0)
                print(device_name, device_ip, device_mac)



if __name__ == '__main__':
    scanner = NetworkScanner()
    subnet = scanner.get_subnet()
    scanner.scan(subnet)