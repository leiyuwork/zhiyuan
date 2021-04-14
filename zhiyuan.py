import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
import itchat
import yagmail


def toeic():
    ur1 = 'https://www.iibc-global.org/toeic/test/lr/guide01'
    web_data = requests.get(ur1)

    # 设为utf-8编码，预防乱码
    web_data.encoding = 'utf-8'
    # print(web_data.text)
    soup = BeautifulSoup(web_data.text, 'html.parser')
    title = soup.select("#anchor01")

    first = soup.select("div.mod-schedule-vertical_head > p")
    second = soup.select("div.mod-schedule-vertical_main_info > p")
    third = soup.select("div.mod-schedule-vertical_sub_body > p")

    result = "【TOEIC官网报名信息推送】\n\n" + title[0].get_text() + ":" + "\n" + first[0].get_text() \
             + "\n" + second[0].get_text() + "\n" + second[1].get_text() + "\n" + second[
                 2].get_text() + "\nインターネット申込受付期間 ｜ " + third[0].get_text() + "\n\n" \
             + first[1].get_text() + "\n" \
             + second[3].get_text() + "\n" \
             + second[4].get_text() + "\n" \
             + second[5].get_text() + "\n" \
             + "インターネット申込受付期間 ｜ " + third[1].get_text() + "\n\n" \
             + first[2].get_text() + "\n" \
             + second[6].get_text() + "\n" \
             + second[7].get_text() + "\n" \
             + second[8].get_text() + "\n" \
             + "インターネット申込受付期間 ｜ " + third[2].get_text() + "\n\n" \
             + "TOEIC报名信息以官网为准，报名请参照以下网址:" + "\nhttps://www.iibc-global.org/toeic/test/lr/guide01.html"
    print(result)
    try:
        chatroomName = '致远'
        itchat.get_chatrooms(update=True)
        chatrooms = itchat.search_chatrooms(name=chatroomName)
        print(chatrooms)

        if len(chatrooms) <= 0:
            print('没有找到群聊:' + chatroomName)
        else:
            chatroom01 = chatrooms[0]['UserName']
            chatroom02 = chatrooms[1]['UserName']
            chatroom03 = chatrooms[2]['UserName']
            chatroom04 = chatrooms[-1]['UserName']

            print(chatroom01)
            print(chatroom02)
            print(chatroom03)
            print(chatroom04)

        itchat.send(result, toUserName=chatroom01)
        itchat.send(result, toUserName=chatroom02)
        itchat.send(result, toUserName=chatroom03)
        itchat.send(result, toUserName=chatroom04)
    except:
        yag = yagmail.SMTP(user="zhiyuanrobot@sina.com", password="wb51583255", host="smtp.sina.com")
        message = ["托业脚本有点问题"]
        print(message)
        yag.send(to="1083358357@qq.com", subject="【致远脚本出错】toeic", contents=message)


def nikkei():
    url = 'https://www.nikkei.com/business/'
    web_data = requests.get(url)

    # 设为utf-8编码，预防乱码
    web_data.encoding = 'utf-8'
    # print(web_data.text)
    soup = BeautifulSoup(web_data.text, 'html.parser')
    xinwen_final = []
    for ultag in soup.find_all('ul', {'class': 'k-hub-list'}):
        for divtag in ultag.find_all('div', {'class': 'k-hub-list__item-content k-hub-list__item-content--numbered'}):
            for a in divtag.find_all('a', href=True):
                xinwen = a.text.lstrip() + "\n" + "https://www.nikkei.com/" + a['href'] + "\n"
                xinwen_final.append(xinwen.replace("?n_cid=TPRN0026", ""))
                break
    b = "本日の日経新聞　「ビジネス」記事アクセスランキングTOP5位 \n\n" + "\n".join(xinwen_final)
    print(b)
    try:
        chatroomName = '致远'
        itchat.get_chatrooms(update=True)
        chatrooms = itchat.search_chatrooms(name=chatroomName)
        print(chatrooms)

        if len(chatrooms) <= 0:
            print('没有找到群聊:' + chatroomName)
        else:
            chatroom01 = chatrooms[0]['UserName']
            chatroom02 = chatrooms[1]['UserName']
            chatroom03 = chatrooms[2]['UserName']
            chatroom04 = chatrooms[-1]['UserName']

            print(chatroom01)
            print(chatroom02)
            print(chatroom03)
            print(chatroom04)

        itchat.send(b, toUserName=chatroom01)
        itchat.send(b, toUserName=chatroom02)
        itchat.send(b, toUserName=chatroom03)
        itchat.send(b, toUserName=chatroom04)
    except:
        yag = yagmail.SMTP(user="zhiyuanrobot@sina.com", password="wb51583255", host="smtp.sina.com")
        message = ["日経脚本有点问题"]
        print(message)
        yag.send(to="1083358357@qq.com", subject="【致远脚本出错】日経", contents=message)


itchat.auto_login(hotReload=True)
scheduler = BlockingScheduler()
scheduler.add_job(toeic, 'cron', day_of_week='sat', hour=8, minute=30)
scheduler.add_job(nikkei, 'cron',  hour=8, minute=30)

scheduler.start()
