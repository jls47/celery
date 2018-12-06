from urllib.request import urlopen
import json, threading
import os
import time
from tasks import *

def run_check():
	x = True
	while x == True:
		
		data = urlopen("http://hollandamerica.jlukes.com/api/view/program_request/").read().decode("utf-8")
		returned = json.loads(data)

		with open("data.txt", "r+") as f:
			data = f.read()
			print(data)
			for object in returned["objects"]:
				print(object)
				if object["id"] not in data:
					f.write(object["id"] + ", ")
					if object["program"] == "portscrape":
						pscrape.delay([object["language"], object["region"], object["email"]])
					else:
						exscrape.delay([object["language"], object["region"], object["email"]])

				else:
					print(object["id"])
		time.sleep(300)


run_check()

#celery -A tasks worker --loglevel=info