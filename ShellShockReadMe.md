![Operation ShellShock](https://github.com/DJ2989/ShellshockProject/blob/main/Images/Operation_Shellshock_art.PNG)


We were successfully able to run the ShellShock exploit on a vulnerable machine using our automated code [nmap_scanner.py](https://github.com/DJ2989/ShellshockProject/blob/main/nmap_scanner.py).  Let's take a look behind the scenes as to how Operation ShellShock works.   

***

In order for Operation ShellShock to work properly, there are a few different pieces of information that we need to capture:

1. **NMAP** with Python

  - Run NMAP on a specific IP Address or scan a network to find one with an open port 80***

2. **DIRB** with Python

  - Run DIRB on the NMAP resulting IP Address to scan for vulnerable file

3. **ShellShock Exploit** with Python

  - Using the IP Address found from NMAP and the vulnerable directory and file found using DIRB, run the ShellShock Exploit using that information

## NMAP Scanning

<details> 
  <summary>Why run NMAP?
  </summary>
NMAP is used in this case to scan the network for machines with an open port 80

</details>

<details>
  <summary>But wait, why do we specifically need port 80?
  </summary>


  Port 80 is a Web server used to identify requests for a web page, specifically web pages using HTTP...

</details>

![NMAP SCAN](https://github.com/DJ2989/ShellshockProject/blob/main/Images/NMAP_NOT_Parsed.JPG)

  -  When NMAP is ran using the command shown below, it scans the network we input and searches specifically for IP Address with an open port 80

    Once we have an IP Address with open port 80, the Python script will automatically input that IP Address into our DIRB command.  
## DIRB Scan
<details> 
  <summary>What is DIRB and why run it?
  </summary>
DIRB is a Web Content Scanner. It looks for existing (and/or hidden) Web Objects. It basically works by launching a dictionary based attack against a web server and analyzing the response. We need DIRB to find a specific folder on web server.

</details>

![DIRB SCAN](https://github.com/DJ2989/ShellshockProject/blob/main/Images/DIRB_NOT_Parsed.JPG)



  - We are using this in order to find directory var/www/cgi-bin/ in order to find any files that have executable permissions. 

                  **Shellshock Vulnerability will ONLY WORK if a file in that folder is found**

  - Once DIRB executes its search and finds file in /cgi-bin folder that comes with a HTTP OK success status response (CODE: 200), It will input that vulnerable file found into Shellshock payload.

## Operation ShellShock
<details> 
  <summary>What is ShellShock?
  </summary>
  Shellshock vulnerability allows an attacker to send operating system commands (bash commands) to web server, thus allowing attacker to take over the web server. 

</details>
  

> **Now at this we have all the needed information to implement the ShellShock exploit**
>
>1.  You will be asked to enter a port number, after the script will open up a terminal with a NetCat listener.
> 
>2. The script will then send a get request with Bash commands embedded in the request to initiate the exploit
> 
>3. At this point you will have a reverse shell terminal opened on the target machine
>



***

## How to run Operation Shellshock Program?

***

#### *This current script is only able to run on Linux(Ubuntu)*
---
#### Software Requirements

  
   - Your system will need to have **Python, Netcat, DIRB** and **Nmap** installed prior to moving forward.
---
#### Using Operation Shellshock

1.  You will need to first need to **download** both *nmap_scanner.py* and *shellshock_script.py*, have them both in the same folder.  
- [nmap_scanner.py](https://github.com/DJ2989/ShellshockProject/blob/main/nmap_scanner.py)
- [shellshock_script.py](https://github.com/DJ2989/ShellshockProject/blob/main/shellshock_script.py)

![File Download](https://github.com/DJ2989/ShellshockProject/blob/main/Images/nmap_file_download.PNG)
 
2. Once you are on the same computer network as target, run nmap_scanner.py by using the following command in a terminal.
- *python nmap_scanner.py*

![Running Operation ](https://github.com/DJ2989/ShellshockProject/blob/main/Images/python_command.PNG)

3. Program will start, press "Enter" key to continue. Type in IP Network address with CIDR notation and push "Enter" key.

![Scan](https://github.com/DJ2989/ShellshockProject/blob/main/Images/Network_address_scan.PNG)

4. At this point script will run and check for machines on network with open TCP 80 ports. If no device detected, script will end.
If machine found, it will continue and initiate a DIRB scan for any files in Cgi-bin folder that exist on machine.
*Exploit will END if no files in that folder are found. Exploit will **NOT WORK** if no files in that folder are found, as it will not be able to execute Shellshock exploit* 

5. At this point program will request what port number you would like to open a listener on your machine for a reverse shell. Enter port number and push "Enter"

![Enter Port](https://github.com/DJ2989/ShellshockProject/blob/main/Images/Port_prompt.PNG)

6. Congratulations! Program has ran succesfully and you should have a reverse shell opened and able to run commands on target machine. 

![Reverse_Shell](https://github.com/DJ2989/ShellshockProject/blob/main/Images/Reverse_Shell.PNG)
