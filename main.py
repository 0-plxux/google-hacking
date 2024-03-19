#(033\[>{})[]
RED = "\033[31m"

OKBLUE = "\033[93m"
OKGREEN = "\033[92m"
BOLD = "\033[1m"
RESET = "\033[0m"
import random
data = []
ip = [] 
a = f"""{OKGREEN}

 ▄▄█▀▀▀▄█                          ▀██             ▀██▀  ▀██▀                 ▀██       ██                   
▄█▀     ▀    ▄▄▄     ▄▄▄     ▄▄▄ ▄  ██    ▄▄▄▄      ██    ██   ▄▄▄▄     ▄▄▄▄   ██  ▄▄  ▄▄▄  ▄▄ ▄▄▄     ▄▄▄ ▄ 
██    ▄▄▄▄ ▄█  ▀█▄ ▄█  ▀█▄  ██ ██   ██  ▄█▄▄▄██     ██▀▀▀▀██  ▀▀ ▄██  ▄█   ▀▀  ██ ▄▀    ██   ██  ██   ██ ██  
▀█▄    ██  ██   ██ ██   ██   █▀▀    ██  ██          ██    ██  ▄█▀ ██  ██       ██▀█▄    ██   ██  ██    █▀▀   
 ▀▀█▄▄▄▀█   ▀█▄▄█▀  ▀█▄▄█▀  ▀████▄ ▄██▄  ▀█▄▄▄▀    ▄██▄  ▄██▄ ▀█▄▄▀█▀  ▀█▄▄▄▀ ▄██▄ ██▄ ▄██▄ ▄██▄ ██▄  ▀████▄ 
                           ▄█▄▄▄▄▀                                                                   ▄█▄▄▄▄▀ 
                                                                                                             
{RESET}
"""
b = """
 ▄▄ •              ▄▄ • ▄▄▌  ▄▄▄ .   ▄ .▄ ▄▄▄·  ▄▄· ▄ •▄ ▪   ▐ ▄  ▄▄ • 
▐█ ▀ ▪ ▄█▀▄  ▄█▀▄ ▐█ ▀ ▪██•  ▀▄.▀·  ██▪▐█▐█ ▀█ ▐█ ▌▪█▌▄▌▪██ •█▌▐█▐█ ▀ ▪
▄█ ▀█▄▐█▌.▐▌▐█▌.▐▌▄█ ▀█▄██ ▪ ▐▀▀▪▄  ██▀▀█▄█▀▀█ ██ ▄▄▐▀▀▄·▐█·▐█▐▐▌▄█ ▀█▄
▐█▄▪▐█▐█▌.▐▌▐█▌.▐▌▐█▄▪▐█▐█▌ ▄▐█▄▄▌  ██▌▐▀▐█▪ ▐▌▐███▌▐█.█▌▐█▌██▐█▌▐█▄▪▐█
·▀▀▀▀  ▀█▄▀▪ ▀█▄▀▪·▀▀▀▀ .▀▀▀  ▀▀▀   ▀▀▀ · ▀  ▀ ·▀▀▀ ·▀  ▀▀▀▀▀▀ █▪·▀▀▀▀ 
"""
inputs = input("Write (help) for more information about the tool or click (enter)..").lower()
if inputs == "help":
    print(f"""
/{OKGREEN}About This Tool{RESET}
|-----------------------------------------------------------------------------------------------
| Uses advanced search operators (Google Dorks) to find juicy information about target websites.
|-----------------------------------------------------------------------------------------------
|
| Uses advanced search operators (Google Dorks) to find juicy information about target websites.
| Every penetration test should start with a passive reconnaissance phase. Since public search
| engines have gathered huge amounts of
| information about almost every website from the Internet, it is a good idea to make some queries and
| get this information from them. Very
| often you will find sensitive information or data that is not supposed to be public.
|
/-----------------------------------------------------------------------------------------------
""")
print(a)
number = int(input(F"""

        /LISTS:
        |--------------------------------------------------------------------------
        | 1) {OKGREEN}Publicly exposed documents{RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 2) {OKGREEN}Directory listing vulnerabilities{RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 3) {OKGREEN}Configuration files exposed{RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 4) {OKGREEN}Database files exposed{RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 5) {OKGREEN}Log files exposed{RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 6) {OKGREEN}Backup and old files{RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 7) {OKGREEN}Login pages{RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 8) {OKGREEN}Find Subdomains{RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 9) {OKGREEN}Find Sub-Subdomains{RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 10) {OKGREEN}SQL errors{RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 11) {OKGREEN}PHP errors / warnings{RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 12) {OKGREEN}phpinfo(){RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 13) {OKGREEN}Search Pastebin.com and other pasting sites{RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 14) {OKGREEN}Search Github.com and Gitlab.com{RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 15) {OKGREEN}Search Stackoverflow.com{RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 16) {OKGREEN}Signup pages{RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 17) {OKGREEN}Search in Wayback Machine{RESET}
        |--------------------------------------------------------------------------
        |--------------------------------------------------------------------------
        | 18) {OKGREEN}Show only IP addresses (opens multiple tabs){RESET}
        |--------------------------------------------------------------------------

Please Enter number:{OKGREEN}
╰┈>>{RESET}"""))
if number == (1):
    print(f"I made my decision {OKGREEN}Publicly exposed documents{RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
        """)
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=site:{ip_adress}+intitle:index.of{RESET}")
if number == (2):
    print(f"I made my decision {OKGREEN}Directory listing vulnerabilities{RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=site:{ip_adress}+intitle:index.of{RESET}")
if number == (3):
    print(f"I made my decision {OKGREEN}Configuration files exposed{RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=site:{ip_adress}+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini+|+ext:env+|+ext:yml+|+ext:json{RESET}")
if number == (4):
    print(f"I made my decision {OKGREEN}Database files exposed{RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=site:{ip_adress}+ext:sql+|+ext:dbf+|+ext:mdb{RESET}")
if number == (5):
    print(f"I made my decision {OKGREEN}Log files exposed{RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=site:{ip_adress}+ext:log{RESET}")
if number == (6):
    print(f"I made my decision {OKGREEN}Backup and old files{RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=site:{ip_adress}+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup{RESET}")
if number == (7):
    print(f"I made my decision {OKGREEN}Login pages{RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=site:{ip_adress}+inurl:login+|+inurl:signin+|+intitle:Login+|+intitle:%22sign+in%22+|+inurl:auth{RESET}")
if number == (8):
    print(f"I made my decision {OKGREEN}Find Subdomains{RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=site:*.{ip_adress}{RESET}")
if number == (9):
    print(f"I made my decision {OKGREEN}Find Sub-Subdomains{RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=site:*.*.{ip_adress}{RESET}")
if number == (10):
    print(f"I made my decision {OKGREEN}SQL errors{RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=site:{ip_adress}+intext:%22sql+syntax+near%22+|+intext:%22syntax+error+has+occurred%22+|+intext:%22incorrect+syntax+near%22+|+intext:%22unexpected+end+of+SQL+command%22+|+intext:%22Warning:+mysql_connect()%22+|+intext:%22Warning:+mysql_query()%22+|+intext:%22Warning:+pg_connect()%22{RESET}")
if number == (11):
    print(f"I made my decision {OKGREEN}PHP errors / warnings{RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=site:{ip_adress}+%22PHP+Parse+error%22+|+%22PHP+Warning%22+|+%22PHP+Error%22{RESET}")
if number == (12):
    print(f"I made my decision {OKGREEN}phpinfo(){RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=site:{ip_adress}+ext:php+intitle:phpinfo+%22published+by+the+PHP+Group%22{RESET}")
if number == (13):
    print(f"I made my decision {OKGREEN}Search Pastebin.com and other pasting sites{RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=site:pastebin.com%20|%20site:paste2.org%20|%20site:pastehtml.com%20|%20site:slexy.org%20|%20site:snipplr.com%20|%20site:snipt.net%20|%20site:textsnip.com%20|%20site:bitpaste.app%20|%20site:justpaste.it%20|%20site:heypasteit.com%20|%20site:hastebin.com%20|%20site:dpaste.org%20|%20site:dpaste.com%20|%20site:codepad.org%20|%20site:jsitor.com%20|%20site:codepen.io%20|%20site:jsfiddle.net%20|%20site:dotnetfiddle.net%20|%20site:phpfiddle.org%20|%20site:ide.geeksforgeeks.org%20|%20site:repl.it%20|%20site:ideone.com%20|%20site:paste.debian.net%20|%20site:paste.org%20|%20site:paste.org.ru%20|%20site:codebeautify.org%20%20|%20site:codeshare.io%20|%20site:trello.com%20%22{ip_adress}%22{RESET}")
if number == (14):
    print(f"I made my decision {OKGREEN}Search Github.com and Gitlab.com{RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=site:github.com%20|%20site:gitlab.com%20%22{ip_adress}%22{RESET}")
if number == (15):
    print(f"I made my decision {OKGREEN}Search Stackoverflow.com{RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=site:stackoverflow.com%20%22{ip_adress}%22{RESET}")
if number == (16):
    print(f"I made my decision {OKGREEN}Signup pages{RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=site:{ip_adress}+inurl:signup+|+inurl:register+|+intitle:Signup{RESET}")
if number == (17):
    print(f"I made my decision {OKGREEN}Search in Wayback Machine{RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://web.archive.org/web/*/{ip_adress}/*{RESET}")
if number == (18):
    print(f"I made my decision {OKGREEN}Show only IP addresses (opens multiple tabs){RESET}")
    ip_adress = input(f"Please Enter my IP Example(00.100.200.00):\n{OKGREEN}╰┈>>>{RESET}")
    if ip_adress :
        print(f"""
        IP: {RED}{ip_adress}{RESET}
        URL: {RED}http://{ip_adress}{RESET}
""")
        ip.append(ip_adress)
        print(f"URL:{RED}https://www.google.com/search?q=({ip_adress})%20(site%3A*.*.29.*%20%7Csite%3A*.*.28.*%20%7Csite%3A*.*.27.*%20%7Csite%3A*.*.26.*%20%7Csite%3A*.*.25.*%20%7Csite%3A*.*.24.*%20%7Csite%3A*.*.23.*%20%7Csite%3A*.*.22.*%20%7Csite%3A*.*.21.*%20%7Csite%3A*.*.20.*%20%7Csite%3A*.*.19.*%20%7Csite%3A*.*.18.*%20%7Csite%3A*.*.17.*%20%7Csite%3A*.*.16.*%20%7Csite%3A*.*.15.*%20%7Csite%3A*.*.14.*%20%7Csite%3A*.*.13.*%20%7Csite%3A*.*.12.*%20%7Csite%3A*.*.11.*%20%7Csite%3A*.*.10.*%20%7Csite%3A*.*.9.*%20%7Csite%3A*.*.8.*%20%7Csite%3A*.*.7.*%20%7Csite%3A*.*.6.*%20%7Csite%3A*.*.5.*%20%7Csite%3A*.*.4.*%20%7Csite%3A*.*.3.*%20%7Csite%3A*.*.2.*%20%7Csite%3A*.*.1.*%20%7Csite%3A*.*.0.*%20){RESET}")
else:
    exit()
