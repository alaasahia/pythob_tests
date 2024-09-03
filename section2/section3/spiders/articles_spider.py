import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from scrapy.http import HtmlResponse
import time
from typing import Optional

class ArticlesSpiderSpider(scrapy.Spider):
    name = 'articles_spider'
    allowed_domains = ['france24.com']
    start_urls = ['https://www.france24.com/en/tag/algeria/']

    def __init__(self, max_pages: Optional[int] = None, *args, **kwargs):
        super(ArticlesSpiderSpider, self).__init__(*args, **kwargs)

        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ), 
            options=chrome_options
        )


    def start_requests(self):
        for url in self.start_urls:
            self.driver.get(url)
            # Wait for 5 seconds for the results to load
            time.sleep(5)  

            html = self.driver.page_source
            response = HtmlResponse(url=url, body=html, encoding='utf-8')

            yield from self.parse(response)


    def parse(self, response):
        # Fetching the articles
        articles = response.css('div.o-layout-list__item.l-m-100.l-t-50.l-d-33 a')
        for article in articles[:5]:              
            title = article.css('h2::text').get()
            url = article.css('::attr(href)').get()
            full_url = response.urljoin(url)              
            print(f'title: {title}, url: {full_url}')









