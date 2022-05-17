# Extracting Trustpilot.com reviews for www.starbucks.com

from selenium import webdriver
import time
from bs4 import BeautifulSoup

test_url = 'https://www.trustpilot.com/review/www.starbucks.com'

option = webdriver.ChromeOptions()
path = '/workspace/twitter_topic_analysis_dashboard/chromedriver'
browser = webdriver.Chrome(path, options=option)
browser.get(test_url)
html_source = browser.page_source
browser.close()

