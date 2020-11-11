from bs4 import BeautifulSoup
import lxml
from urllib.request import Request, urlopen
import re
import os
import json
import tinydb
import svapi

date = "111120" #ONLY EDIT THIS, DDMMYY

svidcount = 0
duplicount = 0

def jsoncleaner(filename):
    with open(filename) as infile:
        jsondirty = json.load(infile)

    os.remove(filename)

    with open(filename, "w") as outfile:
        json.dump(jsondirty, outfile, indent=2)

svidlist = []
svidlist1 = []
urllist = [
    "https://spookvooper.com/user/search/a", 
    "https://spookvooper.com/user/search/b", 
    "https://spookvooper.com/user/search/c", 
    "https://spookvooper.com/user/search/d", 
    "https://spookvooper.com/user/search/e", 
    "https://spookvooper.com/user/search/f", 
    "https://spookvooper.com/user/search/g", 
    "https://spookvooper.com/user/search/h", 
    "https://spookvooper.com/user/search/i", 
    "https://spookvooper.com/user/search/j", 
    "https://spookvooper.com/user/search/k", 
    "https://spookvooper.com/user/search/l", 
    "https://spookvooper.com/user/search/m", 
    "https://spookvooper.com/user/search/n", 
    "https://spookvooper.com/user/search/o", 
    "https://spookvooper.com/user/search/p", 
    "https://spookvooper.com/user/search/q", 
    "https://spookvooper.com/user/search/r", 
    "https://spookvooper.com/user/search/s", 
    "https://spookvooper.com/user/search/t", 
    "https://spookvooper.com/user/search/u", 
    "https://spookvooper.com/user/search/v", 
    "https://spookvooper.com/user/search/w", 
    "https://spookvooper.com/user/search/x", 
    "https://spookvooper.com/user/search/y", 
    "https://spookvooper.com/user/search/z", 
    "https://spookvooper.com/user/search/0", 
    "https://spookvooper.com/user/search/1", 
    "https://spookvooper.com/user/search/2", 
    "https://spookvooper.com/user/search/3", 
    "https://spookvooper.com/user/search/4", 
    "https://spookvooper.com/user/search/5", 
    "https://spookvooper.com/user/search/6", 
    "https://spookvooper.com/user/search/7", 
    "https://spookvooper.com/user/search/8", 
    "https://spookvooper.com/user/search/9"
]


for url in urllist:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")
    
    for link in soup.findAll('a'):
        linkget = str(link.get('href'))
        if "/User/Info?svid=" in linkget:
            linkget = linkget.replace("/User/Info?svid=", "")
            svidlist1.append(linkget)
            svidcount += 1
            print("Getting SVIDS: ", end='')
            print(f"{svidcount} / {url}")

for svid in svidlist1:
    if svid not in svidlist:
        svidlist.append(svid)
    duplicount += 1
    print("Removing duplicate SVIDs: ", end='')
    print(f"{duplicount} / {len(svidlist1)}")

svidlist.sort()

os.remove('svidlist.txt')

with open("svidlist.txt", 'a') as outfile:
    json.dump(svidlist, outfile, indent=2)


db = tinydb.TinyDB("database.json")
table = db.table(name="SV User Data")

database = {}

for i in range(0, len(svidlist)):
    try:
        svid = svidlist[i]
        userdatabasedict = svapi.GetUserDataFromSVID(svid)
        dayssincelastmove = svapi.GetDaysSinceLastMoveFromSVID(svid)
        userdatabasedict["dayssincelastmove"] = dayssincelastmove
        rolelist = svapi.GetDiscordRolesFromSVID(svid)
        userdatabasedict["discordroles"] = rolelist
    except json.decoder.JSONDecodeError:
        userdatabasedict["discord_id"] = None
        userdatabasedict["discordroles"] = []

    try:
        database[svid][date] = userdatabasedict
    except KeyError:
        database[svid] = {}
        database[svid][date] = userdatabasedict

    print("Getting data: ", end='')
    print(f"{i} / {len(svidlist)}")

table.insert(database)

db.close()

jsoncleaner("database.json")
