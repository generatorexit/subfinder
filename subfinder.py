import optparse
import requests

reset = '\033[0m'
red = '\033[91m'
green = '\033[92m'
cyan = '\033[96m'
try:
    def user_input():
        parse_object = optparse.OptionParser()
        parse_object.add_option("-t", dest="target_domain", help="enter a domain")
        options = parse_object.parse_args()[0]

        if not options.target_domain:
            print(red + "\nYou must write a domain." + reset)
            quit()
        else:
            print(cyan + "\nSubFinder started to research..." + reset)

        return options

    target_info = user_input()
    target = target_info.target_domain
    file = open("subdomains.txt")
    c = file.read()
    subdomains = c.splitlines()

    def find_subdomains(target):
        for subdomain in subdomains:
            url = f"http://{subdomain}.{target}"
            try:
                r = requests.get(url)
            except requests.ConnectionError:
                pass
            else:
                print(green + "\n[+] Discovered subdomains:" + cyan + url + reset)
                print (cyan + url + green +"'s status code => "+ str(r.status_code) + reset)

                with open("discovered.txt","a") as discovered_file:
                    discovered_file.write("\n" + url)
                    discovered_file.close()

    find_subdomains(target)
    print(green+"\nFinished!"+ reset)
except KeyboardInterrupt:
    print(green + "\nIt is closed." + reset)