from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from spiders.getlastpostdate_spider import DivarSpider

from twisted.internet.task import LoopingCall
from twisted.internet import reactor


from scrapy.utils.log import configure_logging



configure_logging()
settings = get_project_settings()
settings.set('USER_AGENT','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')
runner = CrawlerRunner(settings)
task = LoopingCall(lambda: runner.crawl(DivarSpider()))
task.start(60 * 10)
reactor.run()