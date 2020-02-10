import requests
from pprint import pprint
from lxml import html

def insert(where, pool):
    db = client[where]
    docs = db.docs
    result = docs.insert_many(pool)

main_link = 'https://news.mail.ru/incident/'
response = requests.get(main_link)
root = html.fromstring(response.text)



newses = root.xpath("//div[@class='newsitem newsitem_height_fixed js-ago-wrapper js-pgng_item']")
result = []
line = {
	"название источника":"",
	"наименование новости":"",
	"ссылку на новость":"",
	"дата публикации":""
}

for news in newses:
	
    line["дата публикации"] = news.xpath(".//span[@class='newsitem__param js-ago']/@datetime")
    line["название источника"] = news.xpath(".//span[@class='newsitem__param']/text()")
    time = news.xpath(".//span[@class='newsitem__param js-ago']/text()")
    line["наименование новости"] = news.xpath(".//span[@class='newsitem__title-inner']/text()")
    line["ссылку на новость"] = "https://news.mail.ru/"+news.xpath(".//a[@class='newsitem__title link-holder']/@href")[0]
    result.append(line)
    print(fromname,day,time,name, link)


client = MongoClient('mongodb://moriska32:6841539@192.168.40.129:27')
insert("news", result)