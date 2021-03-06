import scrapy
from scrapy import Selector
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium_stealth import stealth


class TestSpider(scrapy.Spider):
    name = 'test'

    def start_requests(self):
        yield SeleniumRequest(
            #url="https://www.sustainalytics.com/esg-ratings/?currentpage=1",
            url="https://www.anaf.ro/restante/index.xhtml",
            wait_time=10,
            callback=self.parse
        )

    def parse(self, response):
        driver = response.meta['driver']
        stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
        driver.maximize_window()
        time.sleep(3)
        input()

        # html6 = driver.page_source
        # respObj6 = Selector(text=html6)
        # amntys = respObj6.xpath("//section/div[@class='row']")
        # for amnty in amntys:
        #     chkCmty = amnty.xpath(".//span[contains(text(), 'Community Amenities')]/text()").get()
        #     chkApt = amnty.xpath(".//span[contains(text(), 'Apartment Amenities')]/text()").get()
        #     if chkCmty :
        #         aptAmnty = amnty.xpath(".//ul[contains(@class, 'amenities-list')]/li/text()").getall()
        #         aptAmntyF = "|".join(x.strip() for x in aptAmnty)
        #     elif chkApt :
        #         cmntyAmnty = amnty.xpath(".//ul[contains(@class, 'amenities-list')]/li/text()").getall()
        #         cmntyAmntyF = "|".join(y.strip() for y in cmntyAmnty)
        #     else:
        #         aptAmntyF = None
        #         cmntyAmntyF = None
        #     chkCmty = None
        #     chkApt = None
        # yield{
        #     'aptAmntyF': aptAmntyF,
        #     'cmntyAmntyF': cmntyAmntyF,
        # }


        # driver.execute_script("window.open('');")
        # driver.switch_to.window(driver.window_handles[0])

        # for i in range(2,436):
        #     WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'results mt-5')]/div/div/a")))
        #     time.sleep(2)
        #     html = driver.page_source
        #     respObj = Selector(text=html)

        #     driver.switch_to.window(driver.window_handles[1])
        #     companies = respObj.xpath("//div[contains(@class, 'results mt-5')]/div/div/a")
        #     for company in companies:
        #         url = company.xpath(".//@href").get()
        #         driver.get(f"https://www.sustainalytics.com{url.replace('..', '')}")
        #         html1 = driver.page_source
        #         respObj1 = Selector(text=html1)
        #         yield{
        #             'Identifier': respObj1.xpath("normalize-space(//p[contains(text(), 'Identifier')]/strong/text())").get(),
        #             'Name': respObj1.xpath("normalize-space(//div[contains(@class, 'company-name')]/div/h2/text())").get(),
        #             'Country': respObj1.xpath("normalize-space(//p[contains(text(), 'Country')]/strong/text())").get(),
        #             'Industry': respObj1.xpath("normalize-space(//p[contains(text(), 'Industry')]/strong/text())").get(),
        #             'ESG score': respObj1.xpath("normalize-space(//div[contains(@class, 'risk-rating-score')]/span/text())").get(),
        #             'Industry rank': respObj1.xpath("normalize-space(//strong[@class='industry-group-position']/text())").get(),
        #             'Global rank': respObj1.xpath("normalize-space(//strong[@class='universe-position']/text())").get()
        #         }
        #     driver.switch_to.window(driver.window_handles[0])

        #     driver.get(f"https://www.sustainalytics.com/esg-ratings/?currentpage={i}")