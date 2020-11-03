from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://www.google.com/')

searchbox = driver.find_element_by_xpath(
    '/ html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys("google")
searchbox.send_keys(Keys.ENTER)

# searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')

# searchButton.click()
