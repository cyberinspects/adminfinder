import requests,sys
import threading
from helpers import threadlister

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-u', type=str,required=True,
                    help='Define a target using domain name without any protocls.')

parser.add_argument('-t', type=int,
                    help='Number of threads to work parrallley')

parser.add_argument('-w', type=str,
                    help='Number of threads to work parrallely')

args = parser.parse_args()




print("""
                               (                            
   (     (                     )\ )           (             
   )\    )\ )   )   (         (()/( (         )\ )  (  (    
((((_)( (()/(  (    )\  (      /(_)))\  (    (()/( ))\ )(   
 )\ _ )\ ((_)) )\  ((_) )\ )  (_))_((_) )\ )  ((_)/((_(()\  
 (_)_\(_)_| |_((_)) (_)_(_/(  | |_  (_)_(_/(  _| (_))  ((_) 
  / _ \/ _` | '  \()| | ' \)) | __| | | ' \)/ _` / -_)| '_| 
 /_/ \_\__,_|_|_|_| |_|_||_|  |_|   |_|_||_|\__,_\___||_|   
                                                            
	""")
print("Powered By:@cyberinspects    Author:@kaleemibnanwar\n")

try:
	url=args.u
	threadn=1
	wl='wordlistpure.txt'
	if args.w:
		wl=args.w
	if args.t:
		threadn=args.t

	lives=[]

	def checker(index):
		fd="Not found"
		fdb = str.encode(fd)
		for line in threadlist[index]:
			request = 'http://'+url+'/'+line
			http = requests.get(request)
			code = http.status_code
			if code != 301 and code!= 404:
				if not fdb in http.content:
					print("[+] Page found: "+request)
					lives.append(request)
				else:
					print("[-] Page not found: "+request)
			else:
				print("[-] Page not found: "+ request)




	threads = []
	threadlist=threadlister(str(wl),threadn) 
	for i in range(len(threadlist)):    
	    t = threading.Thread(target=checker, args=(i,))
	    threads.append(t)

	print(f"> {len(threads)} threads has started")
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()
	print("Finished")
	for live in lives:
		print(live)
except Exception as e: 
    print('Operation stopped due to: '+ str(e))





