#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from spiders import DiscoSpiderSpider, AccretechSpiderSpider
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
crawler_process = CrawlerProcess(settings)
spider_clses = [DiscoSpiderSpider, AccretechSpiderSpider]
for spider_cls in spider_clses:
    crawler_process.crawl(spider_cls)

crawler_process.start()