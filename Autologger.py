from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

school_Email_User = "tliddico@ucsc.edu"
school_Email_PW = "Boogies9498"

browser = webdriver.Chrome()
print("made it")
browser.get('http://www.gmail.com')

browser.find_element_by_name("identifier").send_keys(school_Email_User)

browser.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()

browser.implicitly_wait(10)

browser.find_element_by_name("password").send_keys(school_Email_PW)

#browser.implicitly_wait(10)

element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='passwordNext']/content/span"))).click()
#browser.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()

