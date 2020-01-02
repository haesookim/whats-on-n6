from datetime import datetime

from selenium import webdriver
from bs4 import BeautifulSoup

dateString = str(datetime.now())[:10]

url = "https://www.kaist.ac.kr/_prog/fodlst/index.php?site_dvs_cd=kr&menu_dvs_cd=050303&dvs_cd=emp&stt_dt="+dateString+"&site_dvs="

driver = webdriver.Chrome('./chromedriver')
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, "lxml")

meal_table = soup.find("table", class_="menuTb").find_all("td")

driver.close()
lunch_menu = meal_table[1].text
dinner_menu = meal_table[2].text
