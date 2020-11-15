import PySimpleGUI as sg
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import os
import json
from datetime import datetime
import svapi
import webbrowser

def answerreturn(answer):
    if answer == "svid":
        answerlist.append(svid)
    elif answer == "username":
        answerlist.append(userdata["userName"])
    elif answer == "discord id":
        answerlist.append(userdata["discord_id"])
    elif answer == "twitch id":
        answerlist.append(userdata["twitch_id"])
    elif answer == "post likes":
        answerlist.append(userdata["post_likes"])
    elif answer == "comment likes":
        answerlist.append(userdata["comment likes"])
    elif answer == "nationstate":
        answerlist.append(userdata["nationstate"])
    elif answer == "description":
        answerlist.append(userdata["description"])
    elif answer == "credits":
        answerlist.append(userdata["credits"])
    elif answer == "api use count":
        answerlist.append(userdata["api_use_count"])
    elif answer == "minecraft id":
        answerlist.append(userdata["minecraft_id"])
    elif answer == "twitch last message minute":
        answerlist.append(userdata["twitch_last_message_minute"])
    elif answer == "twitch message xp":
        answerlist.append(userdata["twitch_message_xp"])
    elif answer == "twitch messages":
        answerlist.append(userdata["twitch_messages"])
    elif answer == "discord commends":
        answerlist.append(userdata["discord_commends"])
    elif answer == "discord commends sent":
        answerlist.append(userdata["discord_commends_sent"])
    elif answer == "discord last commend hour":
        answerlist.append(userdata["discord_last_commend_hour"])
    elif answer == "discord last commend message":
        answerlist.append(userdata["discord_last_commend_message"])
    elif answer == "discord message xp":
        answerlist.append(userdata["discord_message_xp"])
    elif answer == "discord message count":
        answerlist.append(userdata["discord_message_count"])
    elif answer == "discord last message minute":
        answerlist.append(userdata["discord_last_message_minute"])
    elif answer == "discord warning count":
        answerlist.append(userdata["discord_warning_count"])
    elif answer == "discord ban count":
        answerlist.append(userdata["discord_ban_count"])
    elif answer == "discord kick count":
        answerlist.append(userdata["discord_kick_count"])
    elif answer == "discord game xp":
        answerlist.append(userdata["discord_game_xp"])
    elif answer == "image url":
        answerlist.append(userdata["image_url"])
    elif answer == "days since last move":
        answerlist.append(userdata["dayssincelastmove"])
    elif answer == "discord role id":
        try:
            rolelist = userdata["discordroles"]
            if len(rolelist) > 0:
                roleidlist = []
                for i in range(0, len(rolelist)):
                    roleid = rolelist[i]["id"]
                    roleidlist.append(roleid)
            answerlist.append(roleidlist)
        except:
            pass
    elif answer == "discord role name":
        try:
            rolelist = userdata["discordroles"]
            if len(rolelist) > 0:
                rolenamelist = []
                for i in range(0, len(rolelist)):
                    rolename = rolelist[i]["name"]
                    rolenamelist.append(rolename)
            answerlist.append(rolenamelist)
        except:
            pass

def getkey(keyinput):
    if keyformatter == "svid":
        return "id"
    elif keyformatter == "username":
        return "userName"
    elif keyformatter == "twitch id":
        return "twitch_id"
    elif keyformatter == "discord id":
        return "discord_id"
    elif keyformatter == "post likes":
        return "post_likes"
    elif keyformatter == "comment likes":
        return "comment_likes"
    elif keyformatter == "nationstate":
        return "nationstate"
    elif keyformatter == "description":
        return "description"
    elif keyformatter == "credits":
        return "credits"
    elif keyformatter == "api use count":
        return "api_use_count"
    elif keyformatter == "minecraft id":
        return "minecraft_id"
    elif keyformatter == "twitch last message minute":
        return "twitch_last_message_minute"
    elif keyformatter == "twitch message xp":
        return "twitch_message_xp"
    elif keyformatter == "discord commends":
        return "discord_commends"
    elif keyformatter == "discord commends sent":
        return "discord_commends_sent"
    elif keyformatter == "discord last commend hour":
        return "discord_last_commend_hour"
    elif keyformatter == "discord last commend message":
        return "discord_last_commend_message"
    elif keyformatter == "discord message xp":
        return "discord_message_xp"
    elif keyformatter == "discord message count":
        return "discord_message_count"
    elif keyformatter == "discord warning count":
        return "discord_warning_count"
    elif keyformatter == "discord ban count":
        return "discord_ban_count"
    elif keyformatter == "discord kick count":
        return "discord_kick_count"
    elif keyformatter == "discord game xp":
        return "discord_game_xp"
    elif keyformatter == "image url":
        return "image_url"
    elif keyformatter == "district":
        return "district"
    elif keyformatter == "days since last move":
        return "days_since_last_move"
    elif keyformatter == "discord role id":
        return "discord roles id"
    elif keyformatter == "discord role name":
        return "discord roles name"

def removedupli(inputlist):
    templist = []
    for item in inputlist:
        if item not in templist:
            templist.append(item)
    return templist

helplist = ["Get Data", "Search", "Compare"]
keylistgroup = ["group svid", "group name" , "group name", "group members", "group permission"]
keylist = ["user svid", "username", "twitch id", "discord id", "post likes", "comment likes", "nationstate", "description", "credits", "api use count", "minecraft id", "twitch last message minute", "twitch message xp", "discord commends", "discord commends sent", "discord last commend hour", "discord last commend message", "discord message xp", "discord message count", "discord warning count", "discord ban count", "discord kick count", "discord game xp", "image url", "district", "days since last move", "discord role id", "discord role name"]
operationlist = ["is", "is not", "is less than", "is greater than", "contains"]
modelist = ["AND", "OR", "XOR"]
typelist = ["user svid", "username", "discord id" , "twitch id" ,"minecraft id", "group svid", "group name"]
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
    "https://spookvooper.com/user/search/9", 
    "https://spookvooper.com/group/search/a",
    "https://spookvooper.com/group/search/b", 
    "https://spookvooper.com/group/search/c", 
    "https://spookvooper.com/group/search/d", 
    "https://spookvooper.com/group/search/e", 
    "https://spookvooper.com/group/search/f", 
    "https://spookvooper.com/group/search/g", 
    "https://spookvooper.com/group/search/h", 
    "https://spookvooper.com/group/search/i", 
    "https://spookvooper.com/group/search/j", 
    "https://spookvooper.com/group/search/k", 
    "https://spookvooper.com/group/search/l", 
    "https://spookvooper.com/group/search/m", 
    "https://spookvooper.com/group/search/n", 
    "https://spookvooper.com/group/search/o", 
    "https://spookvooper.com/group/search/p", 
    "https://spookvooper.com/group/search/q", 
    "https://spookvooper.com/group/search/r", 
    "https://spookvooper.com/group/search/s", 
    "https://spookvooper.com/group/search/t", 
    "https://spookvooper.com/group/search/u", 
    "https://spookvooper.com/group/search/v", 
    "https://spookvooper.com/group/search/w", 
    "https://spookvooper.com/group/search/x", 
    "https://spookvooper.com/group/search/y", 
    "https://spookvooper.com/group/search/z", 
    "https://spookvooper.com/group/search/0", 
    "https://spookvooper.com/group/search/1", 
    "https://spookvooper.com/group/search/2", 
    "https://spookvooper.com/group/search/3", 
    "https://spookvooper.com/group/search/4", 
    "https://spookvooper.com/group/search/5", 
    "https://spookvooper.com/group/search/6", 
    "https://spookvooper.com/group/search/7", 
    "https://spookvooper.com/group/search/8", 
    "https://spookvooper.com/group/search/9"
    ]

sg.theme("Mono Green")

mainlayout = [
[sg.Text("SV Data", size=(30, 1), justification="center", font=("Courier New", 24))], 
[sg.Text("Version 2.0", size=(30, 1), justification="center", font=("Courier New", 10))],
[sg.Text("created by Asdia_", size=(30, 1), justification="center", font=("Courier New", 8))],
[sg.Frame("Users and Groups", font=("Courier New", 10), layout=[
[sg.Button("Get Data", key = "main.getdata", font=("Courier New", 10)), sg.Button("Search", key = "main.search", font=("Courier New", 10)), sg.Button("Compare", key="main.compare", font=("Courier New", 10))],])],
[sg.Button("Help and Feedback", key="main.help", font=("Courier New", 10)), sg.Button("Quit", key="main.quit", font=("Courier New", 10))]
]


mainwindow = sg.Window("SV User Data: Main", layout=mainlayout, icon=r"Z:\random stuff\python\sv\userdata\unity-1k.ico", element_justification="c")

while True:
    eventmain, valuemain = mainwindow.read()
    if eventmain == "main.search":
        mainwindow.Hide()
        searchlayout = [
        [sg.Text("Search", size=(30, 1), justification="center", font=("Courier New", 24))], 
        [sg.Multiline(size=(100, 12), auto_refresh=True, autoscroll=True, reroute_stdout=True, key="search.box")], 
        [sg.Text("Search all ", font=("Courier New", 10)), sg.Combo(keylist, default_value="svid", font=("Courier New", 10)), sg.Text(" where ", font=("Courier New", 10)), sg.Combo(keylist, default_value="username", font=("Courier New", 10)), sg.Combo(operationlist, default_value="is", font=("Courier New", 10))],
        [sg.Input("value", size=(10, 1), font=("Courier New", 10)), sg.Text(" on ", font=("Courier New", 10)), sg.Text("date", key="search.date", size=(8, 1), font=("Courier New", 10))],
        [sg.CalendarButton('Choose date', font=("Courier New", 10), target="search.date", format="%d-%m-%Y")],
        [sg.Text("")],
        [sg.Checkbox("Filter out blank responses", default=True, font=("Courier New", 10))],
        [sg.Button("Submit", key = "search.submit", font=("Courier New", 10)), sg.Button("Clear Log", key="search.clear", font=("Courier New", 10)), sg.Button("Cancel", key = "search.cancel", font=("Courier New", 10))]
        ]
        searchwindow = sg.Window("SV User Data: Search", layout=searchlayout, icon=r"Z:\random stuff\python\sv\userdata\unity-1k.ico", element_justification="c")
        while True:
            eventsearch, valuesearch = searchwindow.read()
            if eventsearch == "search.submit":
                answer = valuesearch[0]
                keyformatter = valuesearch[1]
                operator = valuesearch[2]
                value = valuesearch[3]
                date = searchwindow["search.date"].get()
                filterblank = valuesearch[4]
                
                key = getkey(keyformatter)

                try:
                    with open("database.json") as infile:
                        database = json.load(infile)
                except FileNotFoundError:
                    with open("database.json", "a") as infile:
                        infile.write("{}")
                    with open("database.json") as infile:
                        database = json.load(infile)
                
                answerlist = []
                try:
                    for svid in database:
                        userdatalist = database[svid] #list
                        for e in range(0, len(userdatalist)):
                            userdatakey = list(userdatalist[e].keys())
                            if userdatakey[0] == date:
                                userdata = userdatalist[e][date]
                                if value == "null":
                                    value == None
                                if operator == "is":
                                    if key == "discord roles id":
                                        rolelist = userdata["discordroles"]
                                        if len(rolelist) > 0:
                                            for i in range(0, len(rolelist)):
                                                roleid = rolelist[i]["id"]
                                                try:
                                                    int(value)
                                                except:
                                                    raise KeyError
                                                else:
                                                    if int(value) == roleid:
                                                        answerreturn(answer)
                                    elif key == "discord roles name":
                                        rolelist = userdata["discordroles"]
                                        if len(rolelist) > 0:
                                            for i in range(0, len(rolelist)):
                                                rolename = rolelist[i]["name"]
                                                if value == rolename:
                                                    answerreturn(answer)
                                    else:
                                        if value == None:
                                            if userdata[key] == None:
                                                answerreturn(answer)
                                        else:
                                            try:
                                                int(value)
                                            except:
                                                if userdata[key] == value:
                                                    answerreturn(answer)
                                            else:
                                                if userdata[key] == int(value):
                                                    answerreturn(answer)
                                if operator == "is not":
                                    if key == "discord roles id":
                                        rolelist = userdata["discordroles"]
                                        if len(rolelist) > 0:
                                            for i in range(0, len(rolelist)):
                                                roleid = rolelist[i]["id"]
                                                haverole = False
                                                try:
                                                    int(value)
                                                except:
                                                    raise KeyError
                                                else:
                                                    if int(value) == roleid:
                                                        haverole = True
                                                if haverole == False:
                                                    answerreturn(answer)
                                    elif key == "discord roles name":# FIX
                                        rolelist = userdata["discordroles"]
                                        if len(rolelist) > 0:
                                            haverole  = False
                                            for i in range(0, len(rolelist)):
                                                rolename = rolelist[i]["name"]
                                                if value == rolename:
                                                    haverole = True
                                            if haverole == False:
                                                answerreturn(answer)
                                    else:
                                        if value == None:
                                            if userdata[key] == None:
                                                answerreturn(answer)
                                        else:
                                            try:
                                                int(value)
                                            except:
                                                if userdata[key] != value:
                                                    answerreturn(answer)
                                            else:
                                                if userdata[key] != int(value):
                                                    answerreturn(answer)
                                if operator == "is less than": # value is smaller than results (yields all results greater than value)
                                    if key == "discord roles id":
                                        pass
                                    elif key == "discord roles name":
                                        pass
                                    elif key == "svid":
                                        pass
                                    elif key == "username":
                                        pass
                                    elif key == "image url":
                                        pass
                                    else:
                                        try:
                                            int(value)
                                        except:
                                            raise KeyError
                                        else:
                                            if int(value) >= userdata[key]:
                                                answerreturn(answer)
                                if operator == "is greater than": # value is greater than result (yields all results smaller than value)
                                    if key == "discord roles id":
                                        pass
                                    elif key == "discord roles name":
                                        pass
                                    elif key == "svid":
                                        pass
                                    elif key == "username":
                                        pass
                                    elif key == "image url":
                                        pass
                                    else:
                                        try:
                                            int(value)
                                        except:
                                            raise KeyError
                                        else:
                                            if userdata[key] >= int(value):
                                                answerreturn(answer)
                                if operator == "contains":
                                    if key == "discord roles id":
                                        rolelist = userdata["discordroles"]
                                        if len(rolelist) > 0:
                                            for i in range(0, len(rolelist)):
                                                roleid = rolelist[i]["id"]
                                                try:
                                                    int(value)
                                                except:
                                                    raise KeyError
                                                else:
                                                    if int(value) in roleid:
                                                        answerreturn(answer)
                                    elif key == "discord roles name":
                                        rolelist = userdata["discordroles"]
                                        if len(rolelist) > 0:
                                            for i in range(0, len(rolelist)):
                                                rolename = rolelist[i]["name"]
                                                if value in rolename:
                                                    answerreturn(answer)
                                    else:
                                        if str(value) in str(userdata[key]):
                                            answerreturn(answer)
                except KeyError:
                    print("No result could be found.")
                else:
                    if len(answerlist) == 0:
                        print("No result could be found.")
                    else:
                        answerlist = removedupli(answerlist)
                        blankcount = 0
                        for answer in answerlist:
                            if filterblank == True:
                                if answer is not None:
                                    print(answer)
                                else:
                                    blankcount += 1
                            else:
                                print(answer)
                        print("")
                        print(f"{len(answerlist)} results")
                        if filterblank == True:
                            print(f"{blankcount} were blank")
                        print("---")
                            
            if eventsearch == "search.clear":
                searchwindow.FindElement("search.box").Update("")
            if eventsearch == "search.cancel":
                searchwindow.close()
                mainwindow.UnHide()
                break
    if eventmain == "main.getdata":
        mainwindow.Hide()
        getdatalayout = [
        [sg.Text("Get Data", size=(30, 1), justification="center", font=("Courier New", 24))], 
        [sg.Multiline(size=(100, 12), auto_refresh=True, autoscroll=True, reroute_stdout=True, font=("Courier New", 10))], 
        [sg.Text("")],
        [sg.Button("Get Data", key = "getdata.getdata", font=("Courier New", 10)), sg.Button("Cancel", key = "getdata.cancel", font=("Courier New", 10))]
        ]
        getdatawindow = sg.Window("SV User Data: Get Data", layout=getdatalayout, icon=r"Z:\random stuff\python\sv\userdata\unity-1k.ico", element_justification="c")
        while True:
            eventgetdata, valuegetdata = getdatawindow.read()
            if eventgetdata == "getdata.getdata":
                try:
                    with open("database.json") as infile:
                        database = json.load(infile)
                except FileNotFoundError:
                    database = {}
                date = datetime.today().strftime('%Y-%m-%d')
                svidlist = []
                
                svidcount = 0
                
                
                for url in urllist:
                    req = Request(url, headers={'User-Agent': 'Mozilla/4.0'})
                    html_page = urlopen(req)
                    soup = BeautifulSoup(html_page, "html.parser")
                    for link in soup.findAll('a'):
                        svidcount += 1
                        linkget = str(link.get('href'))
                        if "/User/Info?svid=" in linkget:
                            linkget = linkget.replace("/User/Info?svid=", "")
                            svidlist.append(linkget)
                            url = url.replace('https://spookvooper.com/user/search/', '')
                            urltype = "user"
                            print(f"Getting SVIDs       {svidcount}     {urltype}: {url}")
                        elif "/Group/View?groupid=" in linkget:
                            linkget = linkget.replace("/Group/View?groupid=", "")
                            svidlist.append(linkget)
                            url = url.replace('https://spookvooper.com/group/search/', '')
                            urltype = "group"
                            print(f"Getting SVIDs       {svidcount}     {urltype}: {url}")
                
                print("Removing duplicate SVIDs")
                svidlist = removedupli(svidlist)
                
                svidlist.sort()
                try:
                    os.remove('usersvid.txt')
                except:
                    pass
                
                with open("usersvid.txt", 'a') as outfile:
                    json.dump(svidlist, outfile, indent=2)

                usercount = 0
                for i in range(0, len(svidlist)):
                    svid = svidlist[i]
                    try:
                        svapi.GetUserDataFromSVID(svid)
                    except:
                        groupdict={}
                        groupdict["id"] = svid
                        groupdict["name"] = svapi.GetGroupnameFromSVID(svid)
                        
                        memlist = svapi.GetGroupMembersFromSVID(svid)
                        if len(memlist) > 0:
                            groupdict["members"] = memlist
                        else:
                            groupdict["members"] = None
                        
                        todaysdata = {date:groupdict}
                        
                        try:
                            database[svid].append(todaysdata)
                        except KeyError:
                            database[svid] = []
                            database[svid].append(todaysdata)
                    else:
                        try:
                            userdatabasedict = svapi.GetUserDataFromSVID(svid)
                            dayssincelastmove = svapi.GetDaysSinceLastMoveFromSVID(svid)
                            userdatabasedict["dayssincelastmove"] = dayssincelastmove
                            rolelist = svapi.GetDiscordRolesFromSVID(svid)
                            userdatabasedict["discordroles"] = rolelist
                        except json.decoder.JSONDecodeError:
                            userdatabasedict["discord_id"] = None
                            userdatabasedict["discordroles"] = []
                        
                        todaysdata = {date:userdatabasedict}
                        
                        try:
                            database[svid].append(todaysdata)
                        except KeyError:
                            database[svid] = []
                            database[svid].append(todaysdata)
                        
                        
                        
                    usercount += 1
                    
                    print(f"Getting User Data           {usercount}     out of {len(svidlist)}")
                
                try:
                    os.remove("database.json")
                except:
                    pass
                
                with open("database.json", 'a') as outfile:
                    json.dump(database, outfile, indent=2)
                
                print("Successfully retrieved user data! You can view it in database.json.")
            if eventgetdata == "getdata.cancel":
                getdatawindow.close()
                mainwindow.UnHide()
                break
    if eventmain == "main.compare":
        mainwindow.Hide()
        comparelayout = [
        [sg.Text("Compare", size=(30, 1), justification="center", font=("Courier New", 24))], 
        [sg.Text("  Input type: ", font=("Courier New", 10)), sg.Combo(typelist, default_value="user svid", size=(12, 1), font=("Courier New", 10))],
        [sg.Multiline("Input 1", font=("Courier New", 10), size = (50, 6)), sg.Multiline("Input 2", font=("Courier New", 10), size = (50, 6))],
        [sg.Text("   Mode: ", font=("Courier New", 10)), sg.Combo(modelist, default_value="AND", size=(7, 1), font=("Courier New", 10))],
        [sg.Text(" Output type: ", font=("Courier New", 10)), sg.Combo(typelist, default_value="user svid", size=(12, 1), font=("Courier New", 10))],
        [sg.Multiline("", size=(105, 6), key="compare.output", auto_refresh=True, autoscroll=True, reroute_stdout=True, font=("Courier New", 10))],
        [sg.Text("")],
        [sg.Button("Submit", key = "compare.submit", font=("Courier New", 10)), sg.Button("Clear Log", key="compare.clear", font=("Courier New", 10)), sg.Button("Cancel", key="compare.cancel", font=("Courier New", 10))]
        ]
        comparewindow = sg.Window("SV User Data: Compare", layout=comparelayout, icon=r"Z:\random stuff\python\sv\userdata\unity-1k.ico", element_justification="c")
        while True:
            eventcompare, valuecompare = comparewindow.read()
            if eventcompare == "compare.cancel":
                comparewindow.close()
                mainwindow.UnHide()
                break
            if eventcompare == "compare.clear":
                comparewindow["compare.output"].Update("")
            if eventcompare == "compare.submit":
                intype = valuecompare[0]
                input1 = valuecompare[1]
                input2 = valuecompare[2]
                mode = valuecompare[3]
                outputtype = valuecompare[4]
                inputlist1 = []
                inputlist2 = []
                
                answerlist = []

                with open("database.json") as infile:
                    database = json.load(infile)

                inputlist111 = input1.split("\n")
                inputlist211 = input2.split("\n")
                
                inputlist11 = []
                inputlist21 = []
                
                for item in inputlist111:
                    if item != '':
                        inputlist11.append(item)

                for item in inputlist211:
                    if item != '':
                        inputlist21.append(item)

                if intype == "user svid":
                    for svid in inputlist11:
                        if svid != "None":
                            try:
                                svapi.GetBalanceFromSVID(svid)
                            except:
                                pass
                            else:
                                inputlist1.append(svid)
                    for svid in inputlist21:
                        if svid != "None":
                            try:
                                svapi.GetBalanceFromSVID(svid)
                            except:
                                pass
                            else:
                                inputlist2.append(svid)
                if intype == "discord id":
                    for discordid in inputlist11:
                        if discordid != "None":
                            try:
                                svid = svapi.GetSVIDFromDiscord(discordid)
                                inputlist1.append(svid)
                            except:
                                pass
                    for discordid in inputlist21:
                        if discordid != "None":
                            try:
                                svid = svapi.GetSVIDFromDiscord(discordid)
                                inputlist2.append(svid)
                            except:
                                pass
                                
                if intype == "minecraft id":
                    for minecraftid in inputlist11:
                        if minecraftid != "None":
                            try:
                                svid = svapi.GetSVIDFromMinecraft(minecraftid)
                                inputlist1.append(svid)
                            except:
                                pass
                    for minecraftid in inputlist21:
                        if minecraftid != "None":
                            try:
                                svid = svapi.GetSVIDFromMinecraft(minecraftid)
                                inputlist2.append(svid)
                            except:
                                pass

                if intype == "twitch id":
                    for svid in database:
                        numberofdates = len(database[svid])
                        date = list(database[svid][numberofdates-1].keys())[0]
                        userdata = database[svid][numberofdates-1][date]
                    for twitchid in inputlist11:
                        if twitchid != "None":
                            if userdata["twitch_id"] == twitchid:
                                try:
                                    svid = userdata["id"]
                                    inputlist1.append(svid)
                                except:
                                    pass
                    for twitchid in inputlist21:
                        if twitchid != "None":
                            if userdata["twitch_id"] == twitchid:
                                try:
                                    svid = userdata["id"]
                                    inputlist2.append(svid)
                                except:
                                    pass
                if intype == "username":
                    for svid in database:
                        numberofdates = len(database[svid])
                        date = list(database[svid][numberofdates-1].keys())[0]
                        userdata = database[svid][numberofdates-1][date]
                        for username in inputlist11:
                            if username != "None":
                                if userdata["userName"] == username:
                                    try:
                                        svid = userdata["id"]
                                        inputlist1.append(svid)
                                    except:
                                        pass
                        for username in inputlist21:
                            if username != "None":
                                if userdata["userName"] == username:
                                    try:
                                        svid = userdata["id"]
                                        inputlist2.append(svid)
                                    except:
                                        pass

                if intype == "group name":
                    for groupname in inputlist11:
                        if groupname != None:
                            try:
                                svid = svapi.GetSVIDFromGroupname(groupname)
                                inputlist1.append(svid)
                            except:
                                pass
                    for groupname in inputlist21:
                        if groupname != None:
                            try:
                                svid = svapi.GetSVIDFromGroupname(groupname)
                                inputlist2.append(svid)
                            except:
                                pass
                            
                if intype == "group svid":
                    for svid in inputlist11:
                        if svid != "None":
                            result = svapi.DoesGroupExistFromSVID(svid)
                            if result == True:
                                inputlist1.append(svid)
                    for svid in inputlist21:
                        if svid != "None":
                            result = svapi.DoesGroupExistFromSVID(svid)
                            if result == True:
                                inputlist2.append(svid)

                if mode == "AND":
                    for svid in inputlist1:
                        if svid in inputlist2:
                            answerlist.append(svid)
                if mode == "XOR":
                    megalist = inputlist1 + inputlist2
                    megalist = removedupli(megalist)
                    for svid in megalist:
                        if svid in inputlist1 and svid in inputlist2:
                            pass
                        else:
                            answerlist.append(svid)
                if mode == "OR":
                    answerlist = inputlist1 + inputlist2
                
                with open("database.json") as infile:
                    database = json.load(infile)
                
                answerlistfinal = []
                
                for svid in answerlist:
                    try:
                        numberofdates = len(database[svid])
                        date = list(database[svid][numberofdates-1].keys())[0]
                        userdata = database[svid][numberofdates-1][date]
                    except: # group
                        if outputtype == "group svid":
                            answerlistfinal.append(svid)
                        if outputtype == "group name":
                            answerlistfinal.append(svapi.GetGroupnameFromSVID(svid))
                    else:
                        if outputtype == "user svid":
                            answerlistfinal.append(svid)
                        if outputtype == "discord id":
                            answerlistfinal.append(svapi.GetDiscordIdFromSVID(svid))
                        if outputtype == "minecraft id":
                            if userdata["minecraft_id"] == None:
                                answerlistfinal.append("None")
                            else:
                                answerlistfinal.append(userdata["minecraft_id"])
                        if outputtype == "twitch id":
                            if userdata["twitch_id"] == None:
                                answerlistfinal.append("None")
                            else:
                                answerlistfinal.append(userdata["twitch_id"])     
                        if outputtype == "username":
                            username = userdata["userName"]
                            answerlistfinal.append(username)
                if len(answerlistfinal) == 0:
                    print("No result could be found.")
                if len(answerlistfinal) > 0:
                    answerlistfinal = removedupli(answerlistfinal)
                    for answer in answerlistfinal:
                        print(answer)
                    print("")
                    print(f"{len(answerlistfinal)} results")
                print("---")
    if eventmain == "main.help":
        mainwindow.Hide()
        helplayout = [
            [sg.Text("Help and Feedback", size=(30, 1), justification="center", font=("Courier New", 24))], 
            [sg.Frame("Help", font=("Courier New", 10), layout=[
                [sg.Frame("Users and Groups", font=("Courier New", 10), layout=[
                    [sg.Button("Get Data", key="help.getdata", font=("Courier New", 10)), sg.Button("Search", key="help.search", font=("Courier New", 10)), sg.Button("Compare", key="help.compare", font=("Courier New", 10))]
                ])],
                [sg.Frame("Stocks", layout=[
                    
                    # stock help layout
                    
                    
                ])]])],
            [sg.Frame("Feedback", font=("Courier New", 10), layout=[
                [sg.Button("Report a bug", key="help.bug", font=("Courier New", 10)),
                 sg.Button("Request a new feature", key="help.feature", font=("Courier New", 10)),
                 sg.Button("Ask a question", key="help.question", font=("Courier New", 10))]
                            ])],
            [sg.Button("Check for newer version", key="help.version", font=("Courier New", 10))],
            [sg.Text("")],
            [sg.Button("Cancel", key="help.cancel", font=("Courier New", 10))]
        ]
        helpwindow = sg.Window("SV User Data: Help and Feedback", layout=helplayout, icon=r"Z:\random stuff\python\sv\userdata\unity-1k.ico", element_justification="c")
        while True:
            eventhelp, valuehelp = helpwindow.read()
            if eventhelp == "help.version":
                webbrowser.open("https://github.com/asdiapotatisen/SVData/releases")
            if eventhelp == "help.getdata":
                webbrowser.open("https://github.com/asdiapotatisen/SVData/wiki/Get-Data-Menu")
            if eventhelp == "help.search":
                webbrowser.open("https://github.com/asdiapotatisen/SVData/wiki/Search-Menu")
            if eventhelp == "help.compare":
                webbrowser.open("https://github.com/asdiapotatisen/SVData/wiki/Compare-Menu")
            if eventhelp == "help.bug":
                webbrowser.open("https://github.com/asdiapotatisen/SVData/issues/new?assignees=asdiapotatisen&labels=bug&template=bug_report.md&title=")
            if eventhelp == "help.feature":
                webbrowser.open("https://github.com/asdiapotatisen/SVData/issues/new?assignees=asdiapotatisen&labels=enhancement&template=feature_request.md&title=")
            if eventhelp == "help.question":
                webbrowser.open("https://github.com/asdiapotatisen/SVData/issues/new?assigness=asdiapotatisen&labels=question")
            if eventhelp == "help.cancel":
                helpwindow.close()
                mainwindow.UnHide()
                break
    if eventmain == "main.quit":
        break

mainwindow.close()
