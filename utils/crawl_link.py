import scrapy
from scrapy.crawler import CrawlerProcess

class WebsiteCrawler(scrapy.Spider):
    name = "website_crawler"
    allowed_domains = ['docs.opsec.computer']
    start_urls = ['https://docs.opsec.computer/']

    def parse(self, response):
        # Extract data using CSS selectors, XPath, or any method of your choice
        # Example: Extracting all links from the page
        links = response.css('a::attr(href)').getall()
        yield {'url': response.url, 'links': links}

        # Follow internal links and repeat the extraction
        for link in links:
            if link.startswith('/'):
                yield response.follow(link, self.parse)

# Setting up crawler process
def run_crawler():
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output.json',
        # Respect robots.txt policies
        'ROBOTSTXT_OBEY': True,
        # Configure concurrent requests and delay to be polite with the server
        'CONCURRENT_REQUESTS': 16,
        'DOWNLOAD_DELAY': 1,
    })
    process.crawl(WebsiteCrawler)
    process.start()

if __name__ == "__main__":
    run_crawler()