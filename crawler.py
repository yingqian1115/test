#導入模組(module)
import requests
#把ptt八卦版網址存到url變數中
URL = "https://www.ptt.cc/bbs/Stock/index.html"
#設定header跟cookie
my_headers = {"cookie":"over18=1;"}
#發送get請求到ptt八卦版
response = requests.get(URL, headers = my_headers)
#印出回傳網頁程式碼
#print(response.text)
#導入beautifulsoup 模組(module):解析HTML語法工具
import bs4
#把網頁程式碼(HTML)丟到bs4裡分析
soup = bs4.BeautifulSoup(response.text,"html.parser")
'''
<div class="title">
	<a href="/bbs/Stock/M.1642095087.A.886.html">
	[請益] 請問有人參加過股票下市的民事求償嗎?</a>
</div>
'''
#2-2查找所有html元素過濾出標籤名稱為"div",同時class為title
titles = soup.find_all("div","title")
#萃取文字出來
#因為我們有多個Tags存放在 list title
#所以用for迴圈逐筆將list印出來
for t in titles:
    print(t.text)

