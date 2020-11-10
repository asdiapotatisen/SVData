import json

with open("database.json") as infile:
  database = json.load(infile)

mdtext = "# database"

for date in database
  dated = database[date]
  mdtext = mdtext + f"<br><detail><summary>{date}</summary>"
  for username in dated:
    usernamed = database[date][username]
    mdtext = mdtext + f"<br><detail><summary>{username}</summary><br>| Key | Value |"
    for key in username:
      value = database[date][username][key]
      mdtext = mdtext + f"<br>| {key} | {value}|"
    mdtext = mdtext + "</detail>"
  mdtext = mdtext + "</detail>"

with open("database.md", "a") as outfile:
  outfile.write(mdtext)
