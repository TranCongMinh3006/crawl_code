import json
import scrapy
import pandas as pd
from datetime import datetime
# import urllib

OUTPUT_FILENAME = 'output/acbs/acbs_{}.xlsx'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))



link_list = []
title_list=[]
pdf_list=[]
class VnexpressSpider(scrapy.Spider):
    name = 'acbs'
    allowed_domains = ['acbs.com.vn']
    start_urls = ['https://www.acbs.com.vn/tin-tuc/n-a-4728-87']
    CRAWLED_COUNT = 0
    report_id = 4728

    def parse(self, response):
        print("alo alo alo")
        if response.status == 200 and response.css('body::attr("class")').get() == 'page-1 service':
            print('Crawling from:', response.url)
            link = response.url
            title = response.css('div.panel-title > h1.headline::text').get()
            # pdf = 'https://bvsc.com.vn'+ response.css('td.report_row_last > div > a::attr("href")').get()

            link_list.append(link)
            title_list.append(title)
            # pdf_list.append(pdf)

        self.report_id = self.report_id - 1
        print("--------------------------------------------------------------------------")
        print(self.report_id)
        print("--------------------------------------------------------------------------")
        href = self.start_urls[0][:36] + str(self.report_id) + self.start_urls[0][-3:]
        yield response.follow(href,meta = {
                  'dont_redirect': True,
                  'handle_httpstatus_list': [302]
              }, callback=self.parse)

        df = pd.DataFrame({
            'link': link_list,
            'title':title_list
            # 'pdf':pdf_list
        })

        df.to_excel(OUTPUT_FILENAME,encoding='utf8',index = False)