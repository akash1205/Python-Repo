import json
content = open("tweet.txt","r")
with open("stringJson.txt", "wb") as fout:
    json.dump(content, fout, indent=1)
