import subprocess

class NetworkScanner():

    def scan(self):
        result=subprocess.run('sudo nmap -sn -R 192.168.179.0/24')
        print(result.stdout)



if __name__ == '__main__':
    scanner = NetworkScanner
    scanner.scan()