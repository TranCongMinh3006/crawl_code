import json
import scrapy
import pandas as pd
from datetime import datetime
# import urllib

OUTPUT_FILENAME = 'output/acbs/acbs_{}.xlsx'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))



link_list = []
nguon_list=[]
ngay_list=[]
nganh_list=[]
doanh_nghiep_list=[]
pdf_list=[]
class VnexpressSpider(scrapy.Spider):
    name = 'acbs'
    allowed_domains = ['acbs.com.vn']
    start_urls = ['https://www.acbs.com.vn/tin-tuc/n-a-1-87']
    CRAWLED_COUNT = 0
    report_id = 1

    def parse(self, response):
        print("alo alo alo")
        if response.status == 200 and response.css('meta[name="description"]::attr("content")').get() == 'Chi tiết báo cáo':
            print('Crawling from:', response.url)
            link = response.url
            nguon = response.css('[id="ctl00_webPartManager_wp1449244041_wp303232192_lnkSource"]::text').get()
            ngay = response.xpath('//td[contains(@style, "background-color")]/table[contains(@style,"clear")]/tr/td/text()').getall()[1].strip("\r\n ")
            nganh = response.css('[id="ctl00_webPartManager_wp1449244041_wp303232192_lnkSector"]::text').get()
            doanh_nghiep = response.css('[id="ctl00_webPartManager_wp1449244041_wp303232192_lnkSymbol"]::text').get()
            pdf = 'https://bvsc.com.vn'+ response.css('td.report_row_last > div > a::attr("href")').get()

            link_list.append(link)
            nguon_list.append(nguon)
            ngay_list.append(ngay)
            nganh_list.append(nganh)
            doanh_nghiep_list.append(doanh_nghiep)
            pdf_list.append(pdf)

        self.report_id = self.report_id + 1
        print("--------------------------------------------------------------------------")
        print(self.report_id)
        print("--------------------------------------------------------------------------")
        href = self.start_urls[0][:28] + str(self.report_id) + self.start_urls[0][-7:]
        yield response.follow(href,meta = {
                  'dont_redirect': True,
                  'handle_httpstatus_list': [302]
              }, callback=self.parse)

        df = pd.DataFrame({
            'link': link_list,
            'nguon':nguon_list,
            'ngay': ngay_list,
            'nganh':nganh_list,
            'doanh nghiep':doanh_nghiep_list,
            'pdf':pdf_list
        })

        df.to_excel(OUTPUT_FILENAME,encoding='utf8',index = False)