

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

![NMAP SCAN](./images/ARP_scan.png)

  -  When NMAP is ran using the command shown below, it scans the network we input and searches specifically for IP Address with an open port 80

    Once we have an IP Address with open port 80, the Python script will automatically input that IP Address into our DIRB command.  
## DIRB Scan
<details> 
  <summary>What is DIRB and why run it?
  </summary>
DIRB is a Web Content Scanner. It looks for existing (and/or hidden) Web Objects. It basically works by launching a dictionary based attack against a web server and analyzing the response. We need DIRB to find a specific folder on web server.

</details>

![DIRB SCAN](./images/DIRB_SCAN.png)



  - We are using this in order to find directory var/www/cgi-bin/ in order to find any files that have executable permissions. 

                  **Shellshock Vulnerability will ONLY WORK if a file in that folder is found**

  - Once DIRB executes its search and finds file in /cgi-bin folder that comes with a HTTP OK success status response (CODE: 200), It will input that vulnerable file found into Shellshock payload.

## Operation ShellShock
<details> 
  <summary>What is ShellShock?
  </summary>
  Shellshock vulnerability allows an attacker to send operating system commands (bash commands) to web server, thus allowing attacker to take over the web server. 

</details>
  

> Now at this we have all the needed information to implement the ShellShock exploit
> 1.  
> 2.
> 3.
>
![Packet Sniffing](./images/login_sniffed.png)

    This packet sniffer will only capture data that is sent in HTTP, but we can grab this data without the target ever even knowing.

4. Setting up the listener...etc 

Insert screenshot here 

    Explain screenshot here

<details> 

  <summary>Why is it much easier for us to steal HTTP data as opposed to HTTPS?

  </summary>

If you're thinking SSL certificates you are indeed correct! HTTP and HTTPS are the same protocol, however HTTPS has an additonal layer of security. Even if we were to capture HTTPS data we still could read it. (we'll not yet at least. Stay posted for a script to help us sidestep the HTTPS protocol)

</details>

***

## File Intercepting with Python

What are the steps to file intercepting?

    1. Our target makes an HTTP request to download a file

    

    2. We modify/replace the request without our target knowing

<details> 

  <summary>For what purpose would we want to replace our target's download file, with a file of our own?

  </summary>

For malware injection and execution.

</details>

1. Now that we have successfully put ourselves in between the gateway router and our target IP, and we are monitoring our targets HTTP request we want to look for a download request/reponse

