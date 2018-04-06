import sh as bada 
import sys
from colorama import Fore, Back,Style



print """


 /$$   /$$ /$$$$$$$$ /$$$$$$$$ /$$      /$$  /$$$$$$  /$$$$$$$  /$$   /$$       /$$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
| $$$ | $$| $$_____/|__  $$__/| $$  /$ | $$ /$$__  $$| $$__  $$| $$  /$$/      | $$__  $$| $$__  $$ /$$__  $$| $$__  $$| $$_____/| $$__  $$
| $$$$| $$| $$         | $$   | $$ /$$$| $$| $$  \ $$| $$  \ $$| $$ /$$/       | $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$      | $$  \ $$
| $$ $$ $$| $$$$$      | $$   | $$/$$ $$ $$| $$  | $$| $$$$$$$/| $$$$$/        | $$$$$$$/| $$$$$$$/| $$  | $$| $$$$$$$ | $$$$$   | $$$$$$$/
| $$  $$$$| $$__/      | $$   | $$$$_  $$$$| $$  | $$| $$__  $$| $$  $$        | $$____/ | $$__  $$| $$  | $$| $$__  $$| $$__/   | $$__  $$
| $$\  $$$| $$         | $$   | $$$/ \  $$$| $$  | $$| $$  \ $$| $$\  $$       | $$      | $$  \ $$| $$  | $$| $$  \ $$| $$      | $$  \ $$
| $$ \  $$| $$$$$$$$   | $$   | $$/   \  $$|  $$$$$$/| $$  | $$| $$ \  $$      | $$      | $$  | $$|  $$$$$$/| $$$$$$$/| $$$$$$$$| $$  | $$
|__/  \__/|________/   |__/   |__/     \__/ \______/ |__/  |__/|__/  \__/      |__/      |__/  |__/ \______/ |_______/ |________/|__/  |__/


"""


print (Fore.BLUE+"select options: ")

option=''
web=''

print (Fore.GREEN+"enter nslookup find Ip address of any website: ")

print (Fore.GREEN+"enter whois to find Public information of website: ")

print (Fore.GREEN+"enter ip to find ip address of your computer: ")

print (Fore.GREEN+"enter dig find DNS of your computer: ")

print (Fore.GREEN+"enter nmcli see which connection is active on your computer: ")

print (Fore.GREEN+"enter scan see the device information of your network card ")

print (Fore.GREEN+"enter public to see your public ip address ")



while True :

	option =raw_input("$$")

	if option == "nslookup":
		print(Fore.YELLOW+"enter the website to nslookup: ")
		webar = raw_input()
		print bada.nslookup(webar)

	elif option == "whois":
		print (Fore.YELLOW+"Enter the website to find its public data: ")

		whois_ar = raw_input()
		print bada.whois(whois_ar)

	elif option == "ip" :
		print (Fore.YELLOW+"Finding your system ip address ")

		print bada.ip("addr")

	elif option == "dig":
		print (Fore.YELLOW+"enter the website to find its DNS servers ......")
		dig_ar = raw_input()
		print bada.dig(dig_ar)


	elif option == "nmcli" :
		print (Fore.YELLOW+"To check the information about your connection ..............")
		print bada.nmcli.dev.wifi()

	elif option == "scan" :

		print (Fore.YELLOW+"to find Geeky information about your network card please wait few seconds  !!!!!!!<<<<<!!!!!!!!!")
		print bada.iwlist.scan()

	elif option == "public" :

		print (Fore.YELLOW+"Finding your public ip address please wait.......")

		print bada.curl("ifconfig.co")

	else :

		print (Fore.BLUE+"wrong input try again...")

		sys.exit()













