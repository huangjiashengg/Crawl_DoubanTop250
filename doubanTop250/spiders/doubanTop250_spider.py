import scrapy
from doubanTop250.items import Doubantop250Item
from bs4 import BeautifulSoup
import time
import re


class DoubanTop250Spider(scrapy.Spider):
    name = 'doubanTop250_spider'

    def start_requests(self):
        urls = []
        _url = 'https://movie.douban.com/top250?start={}&filter='
        for page in range(0, 11):
            urls.append(_url.format(page*25))
        for url in urls:
            yield scrapy.Request(url, callback=self.sparse)
            time.sleep(2)

    def sparse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        list = soup.find(class_='grid_view').find_all('li')
        for li in list:
            item = Doubantop250Item()
            item['id'] = li.find(class_='').string
            item['name'] = li.find(class_='title').string
            item['poster_links'] = li.find('a').find('img').get('src')
            string = li.find('p').text.strip().split('\n')
            if re.match(r'导演:(.*)主演:(.*) ', string[0], re.M | re.I) != None:
                item['director'] = re.match(r'导演:(.*)主演:(.*) ', string[0], re.M | re.I).group(1).strip()
            if re.match(r'导演:(.*)主演:(.*) ', string[0], re.M | re.I) != None:
                item['actor'] = re.match(r'导演:(.*)主演:(.*) ', string[0], re.M | re.I).group(2).strip()
            if re.match(r'(.*)\xa0/\xa0(.*)\xa0/\xa0(.*) ', string[1], re.M | re.I) != None:
                item['year'] = re.match(r'(.*)\xa0/\xa0(.*)\xa0/\xa0(.*) ', string[1], re.M | re.I).group(1).strip()
            if re.match(r'(.*)\xa0/\xa0(.*)\xa0/\xa0(.*) ', string[1], re.M | re.I) != None:
                item['country'] = re.match(r'(.*)\xa0/\xa0(.*)\xa0/\xa0(.*) ', string[1], re.M | re.I).group(2).strip()
            if re.match(r'(.*)\xa0/\xa0(.*)\xa0/\xa0(.*) ', string[1], re.M | re.I) != None:
                item['type'] = re.match(r'(.*)\xa0/\xa0(.*)\xa0/\xa0(.*) ', string[1], re.M | re.I).group(3).strip()
            item['score'] = li.find(class_='rating_num').string
            Num_of_appraisers = li.find(class_='star').find_all('span')[3].string
            item['Num_of_appraisers'] = re.match(r'(.*)人评价', Num_of_appraisers, re.M | re.I).group(1).strip()
            if li.find(class_='inq') != None:
                 item['quote'] = li.find(class_='inq').string
        # question_list = response.xpath('//*[@class="grid_view"]')

        # for question in question_list.xpath('./li'):
        #     item = Doubantop250Item()
        #     item['id'] = str(question.xpath('/div/div[1]/em/text()').extract())
        #     item['name'] = str(question.xpath('/div/div[2]/div[1]/a/span[1]/text()').extract())
        #     item['poster_links'] = str(question.xpath('/div/div[1]/a/img/@src').extract())
        #     item['all'] = str(question.xpath('/div/div[2]/div[2]/p[1]/text()').extract())
            # string = question.xpath('/div/div[2]/div[2]/p[1]/text()').extract()
            # item['director'] = [re.match(r'\n.*导演:(.*)主演:(.*) ', string[0], re.M | re.I).group(1).strip()]
            # item['actor'] = [re.match(r'\n.*导演:(.*)主演:(.*) ', string[0], re.M | re.I).group(2).strip()]
            # item['year'] = [re.match(r'\n(.*)\xa0/\xa0(.*)\xa0/\xa0(.*) ', string[1], re.M | re.I).group(1).strip()]
            # item['country'] = [re.match(r'\n(.*)\xa0/\xa0(.*)\xa0/\xa0(.*) ', string[1], re.M | re.I).group(2).strip()]
            # item['type'] = [re.match(r'\n(.*)\xa0/\xa0(.*)\xa0/\xa0(.*) ', string[1], re.M | re.I).group(3).strip()]
            # item['score'] = str(question.xpath('/div/div[2]/div[2]/div/span[2]/text()').extract())
            # item['Num_of_appraisers'] = str(question.xpath('/div/div[2]/div[2]/div/span[4]/text()').extract())
            # item['quote'] = str(question.xpath('/div/div[2]/div[2]/p[2]/span/text()').extract())
            yield item
