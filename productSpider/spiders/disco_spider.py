# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
import scrapy
from scrapy.linkextractors import LinkExtractor
from productSpider.items import PdfDownloadItem


class DiscoSpiderSpider(CrawlSpider):
    name = 'disco_spider'
    allowed_domains = ['disco.co.jp']
    start_urls = ['https://www.disco.co.jp/cn_s/technology/']
    rules = [
        # Rule(LinkExtractor(allow=('../products/index.html?id=dicing',)), callback='parse_product'),
        # Rule(LinkExtractor(allow=('../products/index.html?id=laser',)), callback='parse_product'),
        # Rule(LinkExtractor(allow=('../products/index.html?id=grinding&polishing',)), callback='parse_product'),
        # Rule(LinkExtractor(allow=('../products/index.html?id=planarization',)), callback='parse_product'),
        # Rule(LinkExtractor(allow=('../products/index.html?id=separation',)), callback='parse_product'),
        # Rule(LinkExtractor(allow=('../products/index.html?id=mounting',)), callback='parse_product'),
        # Rule(LinkExtractor(allow=('../products/index.html?id=other',)), callback='parse_product'),
        # Rule(LinkExtractor(allow=('../products/other.html#accessory',)), callback='parse_product'),
        # Rule(LinkExtractor(allow=('../products/tool.html?id=hub&hubless',)), callback='parse_product'),
        # Rule(LinkExtractor(allow=('../products/tool.html?id=grinding_wheel',)), callback='parse_product'),
        # Rule(LinkExtractor(allow=('../products/tool.html?id=dry_wheel',)), callback='parse_product'),
        # Rule(LinkExtractor(allow=('../products/other.html#related',)), callback='parse_product'),
        Rule(LinkExtractor(allow=('https://www.disco.co.jp/cn_s/technology',)), callback='parse_product'),
    ]

    def parse_product(self, response):
        # pro_urls = response.xpath('//div[@id="area_products"]/a/@href')
        pro_urls = response.xpath('//*[@id="products_lineup"]//ul[@class="ul_products"]//a/@href')
        for url in pro_urls:
            url = url.get()
            yield scrapy.Request(response.urljoin(url), self.parse_pro_detail)
        
    def parse_pro_detail(self, response):
        pdf_item = PdfDownloadItem()
        pdf_item['sub_cate'] = response.xpath('//title/text()')[0].get()
        pdf_item['file_name'] = response.xpath('//*[@id="product_header"]/h1/text()').get() + '.pdf'
        pdf_item['file_url'] = response.url
        yield pdf_item
        
        
        

