import json

with open("database.json") as infile:
    db = json.load(infile)

key = input("Key: ")
value = input("Value: ")
answer = input("Entry to be retrieved: ")
dates = input("Date(s): ")

database = db["SV User Data"]

datelist = dates.split(", ")

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

answerlist = []
try:
    for svid in database:
        for date in datelist:
            userdata = database[svid][date]
            if key == "discordrolesid":
                rolelist = database[svid][date]["discordroles"]
                for i in range(0, len(rolelist)):
                    roledict = rolelist[i]
                    roleid = roledict["id"]
                    if int(value) == roleid:
                        answerreturn(answer)
                if len(answerlist) == 0:
                    raise KeyError
            elif key == "discordrolesname":
                rolelist = database[svid][date]["discordroles"]
                for i in range(0, len(rolelist)):
                    roledict = rolelist[i]
                    roleid = roledict["name"]
                    if int(value) == roleid:
                        answerreturn(answer)
                if len(answerlist) == 0:
                    raise KeyError
            else:
                if userdata[key] == value:
                    answerreturn(answer)
                elif userdata[key] == int(value):
                    answerreturn(answer)
except KeyError:
    print("No parameter with inputed value could be found.")
else:
    for i in range(0, len(answerlist)):
        print(answerlist[i])
