#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://sports.bwin.com/de/sports/4/wetten/fußball#categoryIds=192&eventId=&leagueIds=43&marketGroupId=&page=0&sportId=4&templateIds=0.8649061927316986"
driver = webdriver.Chrome()
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

containers = soup.findAll("table", {"class": "marketboard-event-with-header__markets-list"})
