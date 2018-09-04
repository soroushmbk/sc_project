import scrapy
import time
from items import LastPostDateItem



import re




class DivarSpider(scrapy.Spider):
    name = 'divar'
    start_urls = [
        'https://bit.ly/2L2Q4q4',

    ]

    def parse(self, response):
        a = response.xpath('//script/text()').extract()
        jsonInScripts = a[2]
        lastpostdate = int(re.search("\W*lastPostDate[^:]*:\D*(\d+)", jsonInScripts).group(1))
        updatetime = int(time.time())
        originsite = 'https://divar.ir'
        category = int(re.search("\W*categoryId[^:]*:\D*(\d+)", jsonInScripts).group(1))
        lastpostdateItem = LastPostDateItem(lastpostdate=lastpostdate, category=category, originsite=originsite, updatetime=updatetime)
        yield lastpostdateItem