# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from productSpider.items import *


class AccretechSpiderSpider(CrawlSpider):
    name = 'accretech_spider'
    allowed_domains = ['accretech.com.cn']
    start_urls = ['http://accretech.com.cn/product.html']

    rules = [
        # 切割机
        Rule(LinkExtractor(allow=('dicer.html',)), callback='parse_dicer'),
        Rule(LinkExtractor(allow=('blade.html',)), callback='parse_dicer'),
        Rule(LinkExtractor(allow=('probe.html',)), callback='parse_dicer'),
        Rule(LinkExtractor(allow=('polish.html',)), callback='parse_dicer'),
        Rule(LinkExtractor(allow=('highrigid_grinder.html',)), callback='parse_dicer'),
        Rule(LinkExtractor(allow=('cmp.html',)), callback='parse_dicer'),
        Rule(LinkExtractor(allow=('cmm.html',)), callback='parse_dicer'),
        Rule(LinkExtractor(allow=('surfcom.html',)), callback='parse_dicer'),
        Rule(LinkExtractor(allow=('rondcom.html',)), callback='parse_dicer'),
        Rule(LinkExtractor(allow=('opt.html',)), callback='parse_dicer'),
    ]

    # def parse_semicon(self, response):
    #     sub_cates = response.css('div.item_icon.html a[href]')
    #     for sub_cate in sub_cates:
    #         sub_cate_url = sub_cate.attrib.get('href')
    #         if sub_cate_url:
    #             yield scrapy.Request(sub_cate_url)

    def parse_dicer(self, response):
        title = response.xpath('//title/text()')[0].extract()
        file_uris = response.xpath('//div[@class="add_link"]//a/@href')
        for file_uri in file_uris:
            file_uri = file_uri.extract()
            pdf_item = PdfDownloadItem()
            if file_uri.startswith('http'): 
                pdf_item['file_name'] = file_uri.split('/')[-1]
                pdf_item['file_url'] = file_uri 
            else:
                pdf_item['file_name'] = file_uri 
                pdf_item['file_url'] = response.urljoin(file_uri) 
            pdf_item['sub_cate'] = title
            yield pdf_item
