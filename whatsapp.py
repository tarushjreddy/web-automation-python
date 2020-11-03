from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

searchbox = driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]')
searchbox.send_keys("google")
searchbox.send_keys(Keys.ENTER)

# searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')

# searchButton.click()
