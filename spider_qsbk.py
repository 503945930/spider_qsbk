import requests
import time
from bs4 import BeautifulSoup

# print(time.time())
# 当前页码
page_number = 1
# 页码总数
page_count = 5
# 统计数目
list_count = 0
f = open("qsbk.log", 'w+', encoding="utf-8")  # 写入文件
while page_number <= page_count:
    time_span = time.time()  # 时间戳
    url = "http://www.qiushibaike.com/hot/page/" + str(page_number) + "/?s=" + str(time_span)
    r = requests.get(url)
    text = r.text
    soup = BeautifulSoup(text, "lxml")
    try:
        content_list = soup.find_all("div", attrs={"class": "article block untagged mb15"})
        for content in content_list:
            if content.contents[1].text:
                list_count += 1
                print("条数:" + str(list_count), file=f)
                print("作者:" + content.contents[1].contents[3].text.strip(), file=f)  # print(content.contents[])
                print("内容:" + content.contents[3].text.strip(), file=f)

                # for number in content.contents[5].content:
                # if number

                # print("好笑数:" + content.contents[5].find("i", attr={"class": "article block untagged mb15"}).text.strip(), file=f)
                # print("评论数:" + content.contents[7].text.strip(), file=f)
            # img = content.contents[5].find("img")["src"];
            #  有没有图片 好笑数 和评论数 位置 不一样
            if content.contents[5].find("img"):
                print("图片:" + content.contents[5].find("img")["src"].strip(), file=f)
                print("链接:http://www.qiushibaike.com" + content.contents[5].find("a")["href"].strip(), file=f)

                # print(content.contents[7].contents[1].find("i").string)
                print("好笑数:" + content.contents[7].contents[1].find("i").string.strip(), file=f)
                print("评论数:" + content.contents[7].contents[3].find("i").string.strip(), file=f)
            else:
                # print(content.contents[5].contents[1].find("i").string)
                print("好笑数:" + content.contents[5].contents[1].find("i").string.strip(), file=f)
                print("评论数:" + content.contents[5].contents[3].find("i").string.strip(), file=f)
            print("---------------------------------------------------------------------", file=f)

    except requests.RequestException as e:
        print(e)
    page_number += 1
f.close()
