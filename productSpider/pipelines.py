# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
import pdfkit
from productSpider.items import PdfDownloadItem
from productSpider.spiders.accretech_spider import AccretechSpiderSpider
from productSpider.spiders.disco_spider import DiscoSpiderSpider


class ProductspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class PdfPipelineBase(object):
    def __init__(self, file_dir=None):
        if file_dir is None:
            file_dir = os.path.join(os.path.dirname(__file__), 'pdfs')
        self.file_dir = file_dir
        if not os.path.exists(self.file_dir):
            os.mkdir(self.file_dir)

    
class PdfDownloadPipeline(PdfPipelineBase):
    def process_item(self, item, spider):
        if isinstance(item, PdfDownloadItem) and isinstance(spider, AccretechSpiderSpider):
            file_name = item['file_name']
            file_url = item['file_url']
            sub_cate = item['sub_cate']
            file_dir = os.path.join(self.file_dir, sub_cate)
            if not os.path.exists(file_dir):
                os.mkdir(file_dir)
            file_name = os.path.join(file_dir, file_name)
            with open(file_name, 'wb') as f:
                res = requests.get(file_url)
                if res.ok:
                    f.write(res.content)
                else:
                    print("downlown failed: %s" % file_name)
        else:
            return item

        
class PdfFromHtmlPipeline(PdfPipelineBase):
    def process_item(self, item, spider):
        if isinstance(item, PdfDownloadItem) and isinstance(spider, DiscoSpiderSpider):
            file_name = item['file_name']
            file_url = item['file_url']
            sub_cate = item['sub_cate'].split('|')
            sub_cate.pop(0)
            sub_cate = '|'.join(sub_cate)
            file_dir = os.path.join(self.file_dir, sub_cate)
            if not os.path.exists(file_dir):
                os.mkdir(file_dir)
            file_name = os.path.join(file_dir, file_name)
            try:
                pdfkit.from_url(file_url, file_name)
            except Exception as e:
                print("html convert to pdf failed: %s" % e)
        else:
            return item
            

    