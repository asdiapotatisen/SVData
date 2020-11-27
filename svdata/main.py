import PySimpleGUI as sg
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import os
import json
from datetime import datetime
import svapi
from multiprocessing import Pool
import webbrowser
import aiohttp
from aiohttp import ClientSession
import asyncio

droptype = ["File", "File"] # DO NOT CHANGE


async def get_data(svidprefix):
    dontgetdata = False
    if svidprefix == "g-":
        basedict={}
        basedict["id"] = svid
        basedict["name"] = svapi.GetGroupnameFromSVID(svid)
        basedict["balance"] = svapi.GetBalanceFromSVID(svid)
        
        memlist = svapi.GetGroupMembersFromSVID(svid)
        if len(memlist) > 0:
            basedict["members"] = memlist
        else:
            basedict["members"] = None
        
    elif svidprefix == "u-": # USER
        try:
            basedict = svapi.GetUserDataFromSVID(svid)
            dayssincelastmove = svapi.GetDaysSinceLastMoveFromSVID(svid)
            basedict["dayssincelastmove"] = dayssincelastmove
            rolelist = svapi.GetDiscordRolesFromSVID(svid)
            basedict["discordroles"] = rolelist
        except json.decoder.JSONDecodeError:
            if onlydiscord == False:
                basedict["discord_id"] = None
                basedict["discordroles"] = []
            else:
                dontgetdata = True
        
    if dontgetdata == False:
        todaysdata = {date:basedict}
    
        try:
            database[svid].append(todaysdata)
        except KeyError:
            database[svid] = []
            database[svid].append(todaysdata)
def answerreturn(answer):
    if answer == "user svid":
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
    elif answer == "group id":
        answerlist.append(userdata["id"])
    elif answer == "group name":
        answerlist.append(userdata["name"])
    elif answer == "group member":
        answerlist.append(userdata["members"])
    elif answer == "group balance":
        answerlist.append(userdata["balance"])
def getkey(keyformatter):
    if keyformatter == "user svid":
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
    elif keyformatter == "user balance":
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
        return "dayssincelastmove"
    elif keyformatter == "discord role id":
        return "discord roles id"
    elif keyformatter == "discord role name":
        return "discord roles name"
    elif keyformatter == "group id":
        return "id"
    elif keyformatter == "group name":
        return "name"
    elif keyformatter == "group member":
        return "member"
    elif keyformatter == "group balance":
        return "balance"
def removedupli(inputlist):
    return list(dict.fromkeys(inputlist))
keylist = ['api use count', 'comment likes', 'days since last move', 'description', 'discord ban count', 'discord commends', 'discord commends sent', 'discord game xp', 'discord id', 'discord kick count', 'discord last commend hour', 'discord last commend message', 'discord message count', 'discord message xp', 'discord role id', 'discord role name', 'discord warning count', 'district', 'group balance', 'group id', 'group member', 'group name', 'image url', 'minecraft id', 'nationstate', 'post likes', 'twitch id', 'twitch last message minute', 'twitch message xp', 'user balance', 'user svid', 'username']
operationlist = ["is", "is not", "is less than", "is greater than", "contains"]
modelist = ["AND", "OR", "XOR"]
typelist = ['discord id', 'group name', 'group svid', 'minecraft id', 'twitch id', 'user svid', 'username']
urllistuser = [
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
    "https://spookvooper.com/user/search/,"
    ]
urllistgroup = [
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
    "https://spookvooper.com/group/search/9", 
    "https://spookvooper.com/group/search/,"
    ]

sg.theme("Mono Green")

mainlayout = [
[sg.Text("SV Data", size=(30, 1), justification="center", font=("Courier New", 24))], 
[sg.Text("Version 2.0.0", size=(30, 1), justification="center", font=("Courier New", 10))],
[sg.Text("created by Asdia_", size=(30, 1), justification="center", font=("Courier New", 8))],
[sg.Button("Get Data", key = "main.getdata", font=("Courier New", 10)), sg.Button("Search", key = "main.search", font=("Courier New", 10)), sg.Button("Compare", key="main.compare", font=("Courier New", 10))],
[sg.Button("Help and Feedback", key="main.help", font=("Courier New", 10)), sg.Button("Quit", key="main.quit", font=("Courier New", 10))]
]


mainwindow = sg.Window("SV User Data: Main", layout=mainlayout, icon="unity-1k.ico", element_justification="c")

while True:
    eventmain, valuemain = mainwindow.read()
    if eventmain == "main.search":
        mainwindow.Hide()
        searchlayout = [
        [sg.Text("Search", size=(30, 1), justification="center", font=("Courier New", 24))], 
        [sg.Multiline(size=(100, 6), auto_refresh=True, autoscroll=True, reroute_stdout=True, key="search.box", font=("Courier New", 10))], 
        [sg.Text("Search ", font=("Courier New", 10)), sg.Combo(["all", "range: input file", "range: input text"], key="search.type", font=("Courier New", 10), enable_events=True, default_value="all"), sg.Combo(keylist, default_value="user svid", font=("Courier New", 10)), sg.Text(" where ", font=("Courier New", 10)), sg.Combo(keylist, default_value="username", font=("Courier New", 10)), sg.Combo(operationlist, default_value="is", font=("Courier New", 10))],
        [sg.Input("Asdia_", size=(10, 1), font=("Courier New", 10)), sg.Text(" on ", font=("Courier New", 10)), sg.Text(datetime.today().strftime('%d-%m-%Y'), key="search.date", size=(8, 1), font=("Courier New", 10))],
        [sg.CalendarButton('Choose date', font=("Courier New", 10), target="search.date", format="%d-%m-%Y")],
        [sg.Multiline('Input SVIDs', size=(50, 3), key="search.text", font=("Courier New", 10), visible=False)],
        [sg.FileBrowse('Input SVIDs', key="search.file", font=("Courier New", 10), disabled=True, enable_events=True)],
        [sg.Text("")],
        [sg.Checkbox("Filter out blank responses", default=True, font=("Courier New", 10))],
        [sg.Button("Submit", key = "search.submit", font=("Courier New", 10)), sg.Button("Save Result", key="search.save", font=("Courier New", 10)), sg.Button("Clear Log", key="search.clear", font=("Courier New", 10)), sg.Button("Cancel", key = "search.cancel", font=("Courier New", 10))]
        ]
        searchwindow = sg.Window("SV User Data: Search", layout=searchlayout, icon="unity-1k.ico", element_justification="c")
        while True:
            eventsearch, valuesearch = searchwindow.read()
            touchedsearchtype = False
            if eventsearch == "search.file":
                head, tail = os.path.split(valuesearch["search.file"])
                filename = tail.split(".txt")
                searchwindow.FindElement("search.file").Update(filename[0])
            if eventsearch == "search.type":
                touchedsearchtype = True
                searchtype2 = valuesearch["search.type"]
                if searchtype2 == "all":
                    searchtype = 'sall'
                    searchwindow["search.text"].Update(visible=False) # invisible
                    searchwindow["search.file"].Update(disabled=True) # invisible
                if searchtype2 == "range: input file":
                    searchtype = "srangefile"
                    searchwindow.FindElement("search.text").Update(visible=False) # invisible
                    searchwindow.FindElement("search.file").Update(disabled=False) # visible
                if searchtype2 == "range: input text":
                    searchtype = "srangetext"
                    searchwindow.FindElement("search.text").Update(visible=True) # visible
                    searchwindow.FindElement("search.file").Update(disabled=True) # invisible
            if eventsearch == "search.save":
                try:
                    name_file = sg.PopupGetText('Enter Filename') + ".txt"
                except:
                    pass
                else:
                    if name_file != None:
                        try:
                            file1 = open(name_file, 'r+')
                        except FileNotFoundError:
                            with open(name_file, "w+") as outfile:
                                json.dump(answerlist, outfile, indent=2)
            if eventsearch == "search.submit":
                answer = valuesearch[0] # FIX may need a func for answerkey() to return correct key because the droplist may return wrong keys
                if answer == "user balance":
                    answer = "credits"
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
                
                if touchedsearchtype == True:
                    if searchtype == "sall":
                        svidin = []
                        for svid in database:
                            svidin.append(svid)
                    if searchtype == "srangetext":
                        svidin = valuesearch["search.text"]
                        svidin = svidin.strip("\n")
                        svidin = svidin.split(", ")
                        for svid in svidin:
                            if svid[1:2] != "-":
                                svidin.pop(svid)
                    if searchtype == "srangefile":
                        head, tail = os.path.split(valuesearch["search.file"])
                        filename = tail.split(".txt")
                        searchwindow.FindElement("search.file").Update(filename[0])
                        completename = filename[0] + ".txt"
                        try:
                            with open(completename) as infile:
                                svidin = json.load(infile)
                            for svid in svidin:
                                if svid[1:2] != "-":
                                    svidin.pop(svid)
                        except:
                            svidin = []
                else:
                    svidin = []
                    for svid in database:
                        svidin.append(svid)
                    # pop up file selector
                    # database = json.load()
                
                answerlist = []

                for svid in svidin:
                    userdatalist = database[svid] #list
                    for e in range(0, len(userdatalist)):
                        userdatakey = list(userdatalist[e].keys())
                        if userdatakey[0] == date:
                            userdata = userdatalist[e][date]
                            
                            svidprefix = svid[:2]
                            if svidprefix == "g-":
                                svidtype = "group"
                            if svidprefix == "u-":
                                svidtype = "user"
                
                            try:
                                if value == "null":
                                    value == None
                                if svidtype == "group":
                                    if operator == "is":
                                        if key == "members":
                                            memlist = userdata["members"]
                                            memlistval = value.split(", ")
                                            if memlist == memlistval:
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
                                        if key == "members":
                                            memlist = userdata["members"]
                                            memlistval = value.split(", ")
                                            if memlist != memlistval:
                                                answerreturn(answer)
                                        else:
                                            if value == None:
                                                if userdata[key] != None:
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
                                    if operator == "contains":
                                        if key == "members":
                                            memlist = userdata["members"]
                                            memlistval = value.split(", ")
                                            for item in memlistval:
                                                if item in memlist:
                                                    answerreturn(answer)
                                        else:
                                            if str(value) == str(userdata[key]):
                                                answerreturn(answer)
                                    if operator == "is less than":
                                        if key == "balance":
                                            try:
                                                int(value)
                                            except:
                                                pass
                                            else:
                                                if int(value) >= userdata['balance']:
                                                    answerreturn(answer)
                                    if operator == "is greater than":
                                        if key == "balance":
                                            try:
                                                int(value)
                                            except:
                                                pass
                                            else:
                                                if int(value) <= userdata['balance']:
                                                    answerreturn(answer)
                                if svidtype == "user":
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
                                        elif key == "discord roles name":
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
                                pass

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
        [sg.Frame("User", layout=[
            [sg.Check("Only get Users", font=("Courier New", 10)), sg.Check("Only get Users who have Discord", font=("Courier New", 10))]
        ], font=("Courier New", 10))],
        [sg.Frame("Group", layout=[
            [sg.Check("Only get Groups", font=("Courier New", 10))]
        ], font=("Courier New", 10))],
        [sg.Text("")],
        [sg.Check("Create svid.txt", default=True, font=("Courier New", 10))],
        [sg.Button("Get Data", key = "getdata.getdata", font=("Courier New", 10)), sg.Button("Cancel", key = "getdata.cancel", font=("Courier New", 10))]
        ]
        getdatawindow = sg.Window("SV User Data: Get Data", layout=getdatalayout, icon="unity-1k.ico", element_justification="c")
        while True:
            eventgetdata, valuegetdata = getdatawindow.read()
            if eventgetdata == "getdata.getdata":
                onlyuser = valuegetdata[1]
                onlydiscord = valuegetdata[2]
                onlygroup = valuegetdata[3]
                createsvid = valuegetdata[4]
                
                if onlyuser == True:
                    if onlygroup == True:
                        urllist = urllistuser + urllistgroup
                    else:
                        urllist = urllistuser
                
                if onlyuser == False:
                    if onlygroup == False:
                        urllist = urllistuser + urllistgroup
                    else:
                        urllist = urllistgroup

                try:
                    with open("database.json") as infile:
                        database = json.load(infile)
                except FileNotFoundError:
                    database = {}
                date = datetime.today().strftime('%d-%m-%Y')
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
                
                if createsvid == True:
                    try:
                        os.remove('svid.txt')
                    except:
                        pass
                    print("Creating svid.txt")
                    with open("svid.txt", 'a') as outfile:
                        json.dump(svidlist, outfile, indent=2)

                for i in range(0, len(svidlist)):
                    svid = svidlist[i]
                    svidprefix = svid[:2]
                    asyncio.run(get_data(svidprefix))
                    print(f"Getting Data:   {i+1} out of {len(svidlist)}")
                                                
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
        [sg.Drop(["Text", "File"], font=("Courier New", 10), key="compare.drop1", enable_events=True, default_value="File"), sg.Drop(["Text", "File"], key="compare.drop2", font=("Courier New", 10), enable_events=True, default_value="File")],
        [sg.Multiline("Input 1", size=(50, 3), key="compare.t1", font=("Courier New", 10), visible=False), sg.Multiline("Input 2", size=(50, 3), key="compare.t2", font=("Courier New", 10), visible=False)],
        [sg.FileBrowse("Input 1", key="compare.in1", enable_events=True, file_types=(("Text Files", "*.txt"),), disabled=False, font=("Courier New", 10)), sg.FileBrowse("Input 2", key="compare.in2", enable_events=True, file_types=(("Text Files", "*.txt"),), disabled=False, font=("Courier New", 10))],
        [sg.Text("   Mode: ", font=("Courier New", 10)), sg.Combo(modelist, default_value="AND", size=(7, 1), font=("Courier New", 10))],
        [sg.Text(" Output type: ", font=("Courier New", 10)), sg.Combo(typelist, default_value="user svid", size=(12, 1), font=("Courier New", 10))],
        [sg.Multiline("", size=(105, 6), key="compare.output", auto_refresh=True, autoscroll=True, reroute_stdout=True, font=("Courier New", 10))],
        [sg.Text("")],
        [sg.Button("Submit", key = "compare.submit", font=("Courier New", 10)), sg.Button("Save Results", key="compare.save", font=("Courier New", 10)), sg.Button("Clear Log", key="compare.clear", font=("Courier New", 10)), sg.Button("Cancel", key="compare.cancel", font=("Courier New", 10))]
        ]
        comparewindow = sg.Window("SV User Data: Compare", layout=comparelayout, icon="unity-1k.ico", element_justification="c")
        while True:
            eventcompare, valuecompare = comparewindow.read()
            if eventcompare == "compare.in1":
                head, tail = os.path.split(valuecompare["compare.in1"])
                filename = tail.split(".txt")
                comparewindow.FindElement("compare.in2").Update(filename[0])
            if eventcompare == "compare.in2":
                head2, tail2 = os.path.split(valuecompare["compare.in2"])
                filename2 = tail2.split(".txt")
                comparewindow.FindElement("compare.in1").Update(filename2[0])
            if eventcompare == "compare.drop1":
                if valuecompare["compare.drop1"] == "File":
                    droptype[0] = "File"
                    comparewindow.FindElement("compare.in1").Update(disabled=False)
                    comparewindow.FindElement("compare.in1").Update("Input 1")
                    comparewindow.FindElement("compare.t1").Update(visible=False)
                if valuecompare["compare.drop1"] == "Text":
                    droptype[0] = "Text"
                    comparewindow.FindElement("compare.t1").Update(visible=True)
                    comparewindow.FindElement("compare.in1").Update("Input 1")
                    comparewindow.FindElement("compare.in1").Update(disabled=True)
            if eventcompare == "compare.drop2":
                if valuecompare["compare.drop2"] == "File":
                    droptype[1] = "File"
                    comparewindow.FindElement("compare.in2").Update(disabled=False)
                    comparewindow.FindElement("compare.in2").Update("Input 2")
                    comparewindow.FindElement("compare.t2").Update(visible=False)
                if valuecompare["compare.drop2"] == "Text":
                    droptype[1] = "Text"
                    comparewindow.FindElement("compare.in2").Update("Input 2")
                    comparewindow.FindElement("compare.t2").Update(visible=True)
                    comparewindow.FindElement("compare.in2").Update(disabled=True)
            if eventcompare == "compare.save":
                try:
                    name_file = sg.PopupGetText('Enter Filename') + ".txt"
                except:
                    pass
                else:
                    if name_file != None:
                        try:
                            file1 = open(name_file, 'r+')
                        except FileNotFoundError:
                            with open(name_file, "w+") as outfile:
                                json.dump(answerlistfinal, outfile, indent=2)
            if eventcompare == "compare.cancel":
                comparewindow.close()
                mainwindow.UnHide()
                break
            if eventcompare == "compare.clear":
                comparewindow["compare.output"].Update("")
            if eventcompare == "compare.submit":
                intype = valuecompare[0]
                mode = valuecompare[1]
                outputtype = valuecompare[2]
                droptype1 = droptype[0]
                droptype2 = droptype[1]
                
                if droptype1 == "File":
                    try:
                        with open(valuecompare["compare.in1"]) as infile:
                            inputlist11 = json.load(infile)
                    except:
                        inputlist11 = []

                if droptype2 == "File":
                    try:
                        with open(valuecompare["compare.in2"]) as infile:
                            inputlist21 = json.load(infile)
                    except:
                        inputlist21 = []

                if droptype1 == "Text":
                    inputlist11 = valuecompare["compare.t1"]
                    inputlist11 = inputlist11.strip("\n")
                    for item in inputlist11: 
                        if item == "":
                            inputlist11.remove(item)
                            print(inputlist11)
                if droptype2 == "Text":
                    inputlist21 = valuecompare["compare.t2"]
                    inputlist21 = inputlist21.strip("\n")
                    inputlist21 = inputlist21.split(', ')
                    for item in inputlist21: 
                        if item == "":
                            inputlist21.remove(item)
                
                inputlist1 = []
                inputlist2 = []
                answerlist = []

                with open("database.json") as infile:
                    database = json.load(infile)

                if intype == "user svid":
                    for svid in inputlist11:
                        try:
                            svidcheck = svid[1:2]
                            if svidcheck == "-":
                                inputlist1.append(svid)
                        except:
                            pass
                    for svid in inputlist21:
                        try:
                            svidcheck = svid[1:2]
                            if svidcheck == "-":
                                inputlist2.append(svid)
                        except:
                            pass
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
                            try:
                                if userdata["twitch_id"] == twitchid:
                                    try:
                                        svid = userdata["id"]
                                        inputlist1.append(svid)
                                    except:
                                        pass
                            except KeyError:
                                pass
                    for twitchid in inputlist21:
                        if twitchid != "None":
                            try:
                                if userdata["twitch_id"] == twitchid:
                                    try:
                                        svid = userdata["id"]
                                        inputlist2.append(svid)
                                    except:
                                        pass
                            except KeyError:
                                pass
                if intype == "username":
                    for username in inputlist11:
                        try:
                            inputlist1.append(svapi.GetSVIDFromUsername(username))
                        except:
                            pass
                    for username in inputlist21:
                        try:
                            inputlist2.append(svapi.GetSVIDFromUsername(username))
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
                        try:
                            if svid[1:2] == "g-":
                                inputlist1.append(svid)
                        except:
                            pass
                    for svid in inputlist21:
                        try:
                            if svid[1:2] == "g-":
                                inputlist2.append(svid)
                        except:
                            pass
                if mode == "AND":
                    for svid in inputlist1:
                        if svid in inputlist2:
                            print(svid)
                            answerlist.append(svid)
                            inputlist1.remove(svid)
                            inputlist2.remove(svid)
                if mode == "XOR":
                    megalist = inputlist1 + inputlist2
                    megalist = removedupli(megalist)
                    for svid in megalist:
                        if svid in inputlist1:
                            if svid in inputlist2:
                                inputlist1.remove(svid)
                                inputlist2.remove(svid)
                            else:
                                answerlist.append(svid)
                                inputlist1.remove(svid)
                        elif svid in inputlist2:
                            if svid in inputlist1:
                                inputlist1.remove(svid)
                                inputlist2.remove(svid)
                            else:
                                answerlist.append(svid)
                                inputlist2.remove(svid)
                if mode == "OR":
                    megalist = inputlist1 + inputlist2
                    answerlist = removedupli(megalist)
                
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

            [sg.Frame("Help", font=("Courier New", 10), layout=[
                [sg.Button("Get Data", key="help.getdata", font=("Courier New", 10)), sg.Button("Search", key="help.search", font=("Courier New", 10)), sg.Button("Compare", key="help.compare", font=("Courier New", 10))]
            ])],
            [sg.Frame("Feedback", font=("Courier New", 10), layout=[
                [sg.Button("Report a bug", key="help.bug", font=("Courier New", 10)),
                 sg.Button("Request a new feature", key="help.feature", font=("Courier New", 10)),
                 sg.Button("Ask a question", key="help.question", font=("Courier New", 10))]
                            ])],
            [sg.Button("Check for newer version", key="help.version", font=("Courier New", 10))],
            [sg.Text("")],
            [sg.Button("Cancel", key="help.cancel", font=("Courier New", 10))]
        ]
        helpwindow = sg.Window("SV User Data: Help and Feedback", layout=helplayout, icon="unity-1k.ico", element_justification="c")
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
