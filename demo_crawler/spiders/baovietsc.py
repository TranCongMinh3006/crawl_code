import json
import scrapy
from datetime import datetime

OUTPUT_FILENAME = 'output/baovietsc/baovietsc_{}.txt'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))


class VnexpressSpider(scrapy.Spider):
    name = 'baovietsc'
    allowed_domains = ['bvsc.com.vn']
    start_urls = ['https://bvsc.com.vn/ViewReports.aspx?CategoryID=17']
    CRAWLED_COUNT = 0

    def parse(self, response):
        print("alo alo alo")
        if response.status == 200 and response.css('meta[name="description"]::attr("content")').get() == 'Chi tiết báo cáo':
            print('Crawling from:', response.url)
            data = {
                'link': response.url,
                # 'title': response.css('h1.title-detail::text').get(),
                # 'description': response.css('p.description::text').get(),

                # 'content': '\n'.join([
                #     ''.join(c.css('*::text').getall())
                #         for c in response.css('article.fck_detail p.Normal')
                # ]),

                # 'category': response.css('meta[itemprop="articleSection"]::attr("content")').get(),
                # 'pub_date': float(response.css('meta[name="its_publication"]::attr("content")').get()),
                # 'keywords': [
                #     k.strip() for k in response.css('meta[name="keywords"]::attr("content")').get().split(',')
                # ],
                # 'tags': [
                #     k.strip() for k in response.css('meta[name="its_tag"]::attr("content")').get().split(',')
                # ],
            }

            with open(OUTPUT_FILENAME, 'a', encoding='utf8') as f:
                f.write(json.dumps(data, ensure_ascii=False))
                f.write('\n')
                self.CRAWLED_COUNT += 1
                self.crawler.stats.set_value('CRAWLED_COUNT', self.CRAWLED_COUNT)
                print('SUCCESS:', response.url)

        yield from response.follow_all(css='a[href^="https://bvsc.com.vn/ViewReports.aspx?CategoryID=17"]::attr(href), a[href^="/"]::attr(href)', callback=self.parse)
