import PySimpleGUI as sg
from bs4 import BeautifulSoup
import lxml
from urllib.request import Request, urlopen
import re
import os
import json
from datetime import datetime
import svapi

sg.theme("Mono Green")

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
    elif answer == "dayssincelastmove":
        answerlist.append(userdata["dayssincelastmove"])
    elif answer == "discordroles":
        answerlist.append(userdata["discordroles"])
                
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
            
keylist = ["svid", "username", "twitch id", "discord id", "post likes", "comment likes", "nationstate", "description", "credits", "api use count", "minecraft id", "twitch last message minute", "twitch message xp", "discord commends", "discord commends sent", "discord last commend hour", "discord last commend message", "discord message xp", "discord message count", "discord warning count", "discord ban count", "discord kick count", "discord game xp", "image url", "district", "days since last move", "discord role id", "discord role name"]
operationlist = ["is", "is not", "is less than", "is greater than", "contains"]
modelist = ["AND", "OR", "XOR"]
typelist = ["svid", "discord id" , "twitch id" ,"minecraft id"]
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

mainlayout = [
[sg.Text("Main Menu", size = (15, 1))], 
[sg.Button("Get Data", key = "main.getdata"), sg.Button("Search", key = "main.search"), sg.Button("Compare", key="main.compare"), sg.Button("Quit", key="main.quit")]
]


mainwindow = sg.Window("SV User Data: Main", layout=mainlayout).finalize()
mainwindow.maximize()

while True:
    eventmain, valuemain = mainwindow.read()
    if eventmain == "main.search":
        mainwindow.Hide()
        searchlayout = [
        [sg.Text("Search Menu", size = (15, 5))],
        [sg.Multiline(size=(300, 25), auto_refresh=True, autoscroll=True, reroute_stdout=True, key="search.box")], 
        [sg.Text("Search all "), sg.Combo(keylist), sg.Text(" where "), sg.Combo(keylist), sg.Combo(operationlist), sg.Input("value"), sg.Text(" on " ), sg.Input("date")],
        [sg.Text("Date must be in DD-MM-YYYY format.")],
        [sg.Text("")],
        [sg.Button("Submit", key = "search.submit"), sg.Button("Clear Log", key="search.clear"), sg.Button("Cancel", key = "search.cancel")]
        ]
        searchwindow = sg.Window("SV User Data: Search", layout=searchlayout).finalize()
        searchwindow.maximize()
        while True:
            eventsearch, valuesearch = searchwindow.read()
            if eventsearch == "search.submit":
                answer = valuesearch[0]
                keyformatter = valuesearch[1]
                operator = valuesearch[2]
                value = valuesearch[3]
                date = valuesearch[4]
                
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
                        finalanswerlist = []
                        for answer in answerlist:
                            if answer not in finalanswerlist:
                                finalanswerlist.append(answer)
                        for answer in finalanswerlist:
                            print(answer)
                        print(f"Total {len(finalanswerlist})
                            
            if eventsearch == "search.clear":
                searchwindow.FindElement("search.box").Update("")
            if eventsearch == "search.cancel":
                searchwindow.close()
                mainwindow.UnHide()
                mainwindow.maximize()
                break
    if eventmain == "main.getdata":
        mainwindow.Hide()
        getdatalayout = [
        [sg.Text("Get Data Menu", size = (15, 5))], 
        [sg.Multiline(size=(300, 25), auto_refresh=True, autoscroll=True, reroute_stdout=True)], 
        [sg.Text("")],
        [sg.Button("Get Data", key = "getdata.getdata"), sg.Button("Exit", key = "getdata.cancel")]
        ]
        getdatawindow = sg.Window("SV User Data: Get Data", layout=getdatalayout).finalize()
        getdatawindow.maximize()
        while True:
            eventgetdata, valuegetdata = getdatawindow.read()
            if eventgetdata == "getdata.getdata":
                try:
                    with open("database.json") as infile:
                        database = json.load(infile)
                except FileNotFoundError:
                    database = {}

                date = datetime.today().strftime('%d-%m-%Y')

                svidcount = 0
                duplicount = 0

                svidlist = []
                svidlist1 = []
                
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
                            print(f"Getting SVIDs: {svidcount}")
                            getdatawindow.refresh()
                
                for svid in svidlist1:
                    if svid not in svidlist:
                        svidlist.append(svid)
                    duplicount += 1
                    print(f"Removing duplicate SVIDs: {duplicount}, {svidcount-duplicount} SVIDs left")
                    getdatawindow.refresh()
                    
                svidlist.sort()
                os.remove('svidlist.txt')
                
                with open("svidlist.txt", 'a') as outfile:
                    json.dump(svidlist, outfile, indent=2)
                                
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
                    
                    print(f"Getting user data: {i+1}, {len(svidlist)-(i+1)} SVIDs left")
                    
                    todaysdata = {date:userdatabasedict}
                    
                    try:
                        database[svid].append(todaysdata)
                    except KeyError:
                        database[svid] = []
                        database[svid].append(todaysdata)
                        
                os.remove("database.json")
                
                with open("database.json", 'a') as outfile:
                    json.dump(database, outfile, indent=2)
                
                print("Successfully retrieved user data! You can view it in database.json.")
            if eventgetdata == "getdata.cancel":
                getdatawindow.close()
                mainwindow.UnHide()
                mainwindow.maximize()
                break
    if eventmain == "main.compare":
        mainwindow.Hide()
        comparelayout = [
        [sg.Text("Compare Menu", size=(15, 5))],
        [sg.Input("Input type: "), sg.Combo(typelist)],
        [sg.Input("Input 1", size = (145, 25)), sg.Input("Input 2", size = (145, 25))],
        [sg.Text("Mode: "), sg.Combo(modelist)],
        [sg.Text("")],
        [sg.Button("Submit", key = "compare.submit"), sg.Button("Cancel", key="compare.cancel")]
        comparewindow = sg.Window("SV User Data: Compare", layout=comparelayout).finalize()
        comparewindow.maximize()
        while True:
            eventcompare, valuecompare = comparewindow.read()
            if eventcompare == "compare.cancel":
                comparewindow.close()
                mainwindow.unhide()
                mainwindow.maximize()
                break
            if eventcompare == "compare.submit":
                type = valuecompare[0]
                input1 = valuecompare[1]
                input2 = valuecompare[2]
                mode = valuecompare[3]
                inputlist1 = []
                inputlist2 = []
                if type == "svid":
                    inputlist1 = input1.split("\n")
                    inputlist2 = input2.split("\n")
                if type == "discord id":
                    templist1 = input1.split("\n")
                    templist2 = input2.split("\n")
                    for discordid in templist1:
                        svid = svapi.GetSVIDFromDiscordID(discordid)
                        inputlist1.append(svid)
                    for discordid in templist2:
                         svid = svapi.GetSVIDFromDiscordID(discordid)
                         inputlist2.append(svid)
                # do this repeatedly
                # may want to seive out None
                if mode == "AND":
                    for svid in inputlist1:
                        if svid in inputlist2:
                             answerlist.append(svid)
                if mode == "XOR":

                if mode == "OR":

                if len(answerlist) == 0:
                    print("No result could be found.")
                if len(answerlist) > 0:
                    for answer in answerlist:
                        print(answer)
                    print(f"Total: {len(answerlist)}"
                        
    if eventmain == "main.quit":
        break

mainwindow.close()
