from bs4 import BeautifulSoup
import requests
import json

source = requests.get("https://www.nicovideo.jp/watch/sm37486065")
soup = BeautifulSoup(source.text, "html.parser")
elem = soup.select_one("#js-initial-watch-data")
js = json.loads(elem.get("data-api-data"))
threads = js["comment"]["threads"]
print(threads)
#print(json.dumps(js,indent=2))
comments=[]#あつかいやすいりすとでーたにした
for i in range(len(threads)):
    params = {
        "thread": threads[i]["id"],
        "version": "20090904",
        "scores": "1",
        "fork": threads[i]["fork"],
        "language": "0",
        "res_from": "1"
    }
    url = threads[1]["server"] + "/api.json/thread"
    print(params)
    res = requests.get(url, params=params)
    print()
    resjs = json.loads(res.content)
    #print(json.dumps(resjs))
    
    for item in resjs:
        if item.get("chat")==None:
            continue
        comments.append([int(item.get("chat").get("no")),item.get("chat").get("content"),int(item.get("chat").get("vpos")),item.get("chat").get("mail")])
        #print(item.get("chat").get("content"))

comments.sort(key=lambda x:x[2])#時間に沿って並べ替え
print(comments)
print(str(len(comments))+" 件")
for i in range(len(comments)):
    print(comments[i][1])#コメント