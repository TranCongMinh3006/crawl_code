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

import json
import scrapy
from datetime import datetime
# import urllib

OUTPUT_FILENAME = 'output/baovietsc/baovietsc_{}.txt'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))


class VnexpressSpider(scrapy.Spider):
    name = 'baovietsc'
    allowed_domains = ['bvsc.com.vn']
    start_urls = ['https://bvsc.com.vn/Reports/8402/b.aspx']
    CRAWLED_COUNT = 0
    report_id = 0

    def parse(self, response):
        print("alo alo alo")
        if response.status == 200 and response.css('meta[name="description"]::attr("content")').get() == 'Chi tiết báo cáo':
            print('Crawling from:', response.url)
            data = {
                'link': response.url,
                'nguồn':response.css('[id="ctl00_webPartManager_wp1449244041_wp303232192_lnkSource"]::text').get(),
                # 'ngày':response.css('td.NoPadding > table > tbody > tr').getall()[5],
                'ngành':response.css('[id="ctl00_webPartManager_wp1449244041_wp303232192_lnkSector"]::text').get(),
                'pdf':'https://bvsc.com.vn'+ response.css('td.report_row_last > div > a::attr("href")').get(),
            }
            with open(OUTPUT_FILENAME, 'a', encoding='utf8') as f:
                f.write(json.dumps(data, ensure_ascii=False))
                f.write('\n')
                self.CRAWLED_COUNT += 1
                self.crawler.stats.set_value('CRAWLED_COUNT', self.CRAWLED_COUNT)
                print('SUCCESS:', response.url)
        report_id = self.report_id + 1
        href = self.start_urls[0][:28] + str(report_id) + self.start_urls[0][-7:]
        print(href)
        # # href = urllib.quote(href)
        yield response.follow(href, callback=self.parse)