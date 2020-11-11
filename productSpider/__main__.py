#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from spiders import DiscoSpiderSpider, AccretechSpiderSpider
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging


settings = get_project_settings()
crawler_process = CrawlerProcess(settings)
configure_logging(settings)
spider_clses = [DiscoSpiderSpider, AccretechSpiderSpider]
for spider_cls in spider_clses:
    crawler_process.crawl(spider_cls)

crawler_process.start()