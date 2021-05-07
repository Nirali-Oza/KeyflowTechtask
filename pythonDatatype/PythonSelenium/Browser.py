import time

from selenium import webdriver

# Browser exposes an executable files
# Selenium test will invoke this executable file and with help of this we can automatically invoke browser
from selenium.webdriver.chrome.webdriver import WebDriver

driver: WebDriver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")

#maximize browser
driver.maximize_window()
driver.get("https://stage-www.keyflow.com/en/profile/login")

print(driver.title)
print(driver.current_url)

#Enter data to the textboxes
driver.find_element_by_name("phone").send_keys("+46761177777")
driver.find_element_by_name("password").send_keys("testerQA123")
driver.find_element_by_tag_name("BUTTON").click()

#Click on profile
time.sleep(5)
Var = driver.find_element_by_xpath("//header/div[1]/div[2]/nav[1]/ul[1]/li[4]/div[1]/div[3]/div[1]/figure[1]/div[1]").click()
print(driver.current_url)

#To fetch age from profile page

print(driver.find_element_by_xpath("//html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/h1[1]").text)
#//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/h1[1]



















