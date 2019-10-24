import requests
import time
import json
from datetime import timedelta


def ConvertSectoDay(date, n): 
  
    day = n // (24 * 3600) 
  
    n = n % (24 * 3600) 
    hour = n // 3600
  
    n %= 3600
    minutes = n // 60
  
    n %= 60
    seconds = n 
    print("date", date)
    print(day,"days", hour, "hours",  
          minutes, "minutes", 
          seconds, "seconds") 
  
id = 0
intra = input("intra name: ")
URL1 = "https://api.intra.42.fr/v2/users/" + intra
r1 = requests.get(url=URL1, headers={'Authorization': 'Bearer 06f786a5d158a8611beb206dada4a86cdb53f8f785f1edf30aa34fc3230fcdf0'})
response1 = r1.json()
for key, val in response1.items():
	if key == "id":
		id = val
		break
URL = "https://api.intra.42.fr/v2/users/" + str(id) + "/locations"
i = 1
t = 0
# r = requests.get(url=URL, headers={'Authorization': 'Bearer 14ebe327b155184e45f51af24481de93e8c1f41c4662efaf6311ae360f8a9c5d'})
while 1:
	# breakpoint()
	r = requests.get(url=URL, headers={'Authorization': 'Bearer 06f786a5d158a8611beb206dada4a86cdb53f8f785f1edf30aa34fc3230fcdf0'}, params={'page':i})
	i = i + 1 
	if r.status_code == 200:
		response = r.json()
		for resp in response:
			begin = 0
			end = 0
			for key, val in resp.items():
				if key == "end_at":
            # print(type(val))
					tmpEnd = str(val).split("T")
					if len(tmpEnd) > 1:
						end = tmpEnd[1]
				if key == "begin_at":
					tmpBegin = str(val).split("T")
					if len(tmpBegin) > 1:
						begin = tmpBegin[1]
				if begin and end:
					begintmpTime = begin.split(".")
					begintmpTime2 = begintmpTime[0].split(":")
					beginhours = int(begintmpTime2[0])
					beginminutes = int(begintmpTime2[1])
					beginSeconds = int(begintmpTime2[2])
					endtmpTime = end.split(".")
					endtmpTime2 = endtmpTime[0].split(":")
					endhours = int(endtmpTime2[0])
					endminutes = int(endtmpTime2[1])
					endSeconds = int(endtmpTime2[2])
					tmpBeginSubtract = timedelta(hours=beginhours, minutes=beginminutes, seconds=beginSeconds)
					tmpEndSubtract = timedelta(hours=endhours, minutes=endminutes, seconds=endSeconds)
					check = int((tmpEndSubtract - tmpBeginSubtract).total_seconds())
					if check < 0:
						check = check + 86400
					t = t + check
					begin = None
					end = None
					ConvertSectoDay(tmpBegin, t)
					break
		time.sleep(1)
		# breakpoint()
		continue
	else:
		print(i)
		break
t = t * 60
        