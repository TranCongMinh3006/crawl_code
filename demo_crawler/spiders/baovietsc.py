# import json
# import scrapy
# from datetime import datetime

# OUTPUT_FILENAME = 'output/baovietsc/baovietsc_{}.txt'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))


# class VnexpressSpider(scrapy.Spider):
#     name = 'baovietsc'
#     allowed_domains = ['bvsc.com.vn']
#     start_urls = ['https://bvsc.com.vn/ViewReports.aspx?CategoryID=17']
#     CRAWLED_COUNT = 0

#     def parse(self, response):
#         print("alo alo alo")
#         if response.status == 200 and response.css('meta[name="description"]::attr("content")').get() == 'Chi tiết báo cáo':
#             print('Crawling from:', response.url)
#             data = {
#                 'link': response.url
#             }

#             with open(OUTPUT_FILENAME, 'a', encoding='utf8') as f:
#                 f.write(json.dumps(data, ensure_ascii=False))
#                 f.write('\n')
#                 self.CRAWLED_COUNT += 1
#                 self.crawler.stats.set_value('CRAWLED_COUNT', self.CRAWLED_COUNT)
#                 print('SUCCESS:', response.url)

#         yield from response.follow_all(css='a[href^="https://bvsc.com.vn/ViewReports.aspx?CategoryID=17"]::attr(href), a[href^="/"]::attr(href)', callback=self.parse)


#------------------------------------------------------------------------------------------------
# cach nay la cach ajax

# import json
# import scrapy
# from datetime import datetime

# OUTPUT_FILENAME = 'output/baovietsc/baovietsc_{}.txt'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))


# class VnexpressSpider(scrapy.Spider):
#     name = 'baovietsc'
#     allowed_domains = ['bvsc.com.vn']
#     start_urls = ['https://bvsc.com.vn/ViewReports.aspx?CategoryID=17']
#     CRAWLED_COUNT = 0

#     def parse(self, response):
#         print("alo alo alo")
#         if response.status == 200 and response.url =="https://bvsc.com.vn/ViewReports.aspx?CategoryID=17":
#             link = response.css("td:nth-child(3) a::attr(href)").getall()
#             print('Crawling from:', link)
#             data = {
#                 'link': link,
#             }
#             with open(OUTPUT_FILENAME, 'a', encoding='utf8') as f:
#                 f.write(json.dumps(data, ensure_ascii=False))
#                 f.write('\n')
#                 self.CRAWLED_COUNT += 1
#                 self.crawler.stats.set_value('CRAWLED_COUNT', self.CRAWLED_COUNT)
#                 print('SUCCESS:', response.url)
#         yield from response.follow_all(css='a[href^="https://bvsc.com.vn/ViewReports.aspx?CategoryID=17"]::attr(href), a[href^="/"]::attr(href)', callback=self.parse)


#---------------------------------------------------------------------------------------
#  version 1 da haon thien txt
# import json
# import scrapy
# from datetime import datetime
# import time

# OUTPUT_FILENAME = 'output/baovietsc/baovietsc_{}.txt'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))


# class VnexpressSpider(scrapy.Spider):
#     name = 'baovietsc'
#     allowed_domains = ['bvsc.com.vn']
#     start_urls = ['https://bvsc.com.vn/Reports/1/b.aspx']
#     CRAWLED_COUNT = 0
#     report_id = 8000

#     def parse(self, response):
#         print("alo alo alo")
#         # time.sleep(2)
#         if response.status == 200 and response.css('meta[name="description"]::attr("content")').get() == 'Chi tiết báo cáo':
#             print('Crawling from:', response.url)
#             data = {
#                 'link': response.url,
#                 'nguồn': response.css('[id="ctl00_webPartManager_wp1449244041_wp303232192_lnkSource"]::text').get(),
#                 'ngày': response.xpath('//td[contains(@style, "background-color")]/table[contains(@style,"clear")]/tr/td/text()').getall()[1].strip("\r\n "),
#                 'ngành': response.css('[id="ctl00_webPartManager_wp1449244041_wp303232192_lnkSector"]::text').get(),
#                 'doanh_nghiep': response.css('[id="ctl00_webPartManager_wp1449244041_wp303232192_lnkSymbol"]::text').get(),
#                 'pdf':'https://bvsc.com.vn'+ response.css('td.report_row_last > div > a::attr("href")').get(),
#             }
#             with open(OUTPUT_FILENAME, 'a', encoding='utf8') as f:
#                 f.write(json.dumps(data, ensure_ascii=False))
#                 f.write('\n')
#                 self.CRAWLED_COUNT += 1
#                 self.crawler.stats.set_value('CRAWLED_COUNT', self.CRAWLED_COUNT)
#                 print('SUCCESS:', response.url)

#         self.report_id = self.report_id + 1
#         print("--------------------------------------------------------------------------")
#         print(self.report_id)
#         print("--------------------------------------------------------------------------")
#         href = self.start_urls[0][:28] + str(self.report_id) + self.start_urls[0][-7:]
#         yield response.follow(href,meta = {
#                   'dont_redirect': True,
#                   'handle_httpstatus_list': [302]
#               }, callback=self.parse)



# -------------------------------------------------------------------------
import json
import scrapy
import pandas as pd
from datetime import datetime
# import urllib

OUTPUT_FILENAME = 'output/baovietsc/baovietsc_{}.xlsx'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))



link_list = []
nguon_list=[]
ngay_list=[]
nganh_list=[]
doanh_nghiep_list=[]
pdf_list=[]
class VnexpressSpider(scrapy.Spider):
    name = 'baovietsc'
    allowed_domains = ['bvsc.com.vn']
    start_urls = ['https://bvsc.com.vn/Reports/8448/b.aspx']
    CRAWLED_COUNT = 0
    report_id = 8448

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

        self.report_id = self.report_id - 1
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