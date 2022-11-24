import requests
from bs4 import BeautifulSoup
import json

# 加上 Headers 內的 "User-Agent"
""" ref: https://blog.jiatool.com/posts/gamer_ani_spider/
「User-Agent」(使用者代理)簡單來說是要"自我介紹"，說明自己是誰、版本號多少、使用什麼作業系統這類資訊。
例如我這邊是使用 Chrome 瀏覽器、版本為 96.0.4664.45、作業系統為 Windows 10 64 位元。如果你是使用 Android 或 iOS 系統的手機，那它送出去的 User-Agent 也會有所不同。

「User-Agent」算是一個讓伺服器最簡易判斷送出請求的人是誰，是電腦瀏覽器？是手機瀏覽器？還是Google爬蟲？
不過就像我們上面程式操作的，它也很容易自己去更改。
"""
sn = 31951
h = {
'Content-Type':'application/x-www-form-urlencoded;charset=utf-8',
'origin':'https://ani.gamer.com.tw',
'authority':'ani.gamer.com.tw',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
data = {'sn':f'{sn}'}
re = requests.post('https://ani.gamer.com.tw/ajax/danmuGet.php', data=data, headers=h)

if re.status_code == 200:
    print("success request!")
else:
    print(f"fail request QAQ, status code = {re.status_code}")

anime_soup = BeautifulSoup(re.text, "html.parser")
danmu_json = json.loads(re.text) #keys: ['text', 'color', 'size', 'position', 'time', 'sn', 'userid']
class Danmu:
    def __init__(self, sn:int, text:str, userid:str) -> None:
        self._sn = sn
        self.text = text
        self.userid = userid
        return
danmu_obj_list = [Danmu(sn, danmu["text"], danmu["userid"]) if "簽" not in danmu["text"] else None for danmu in danmu_json]
print(danmu_obj_list)
