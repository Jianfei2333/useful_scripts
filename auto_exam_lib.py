#coding: UTF-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
browser.get('http://202.116.65.85/sysulib/')
cardNo = browser.find_element_by_id("cardNo")

if len(sys.argv) == 1:
    Id = raw_input('请输入学生证号:')
    #Id = "15336204"
else:
    Id = str(sys.argv[1])
    #print (Id)

cardNo.send_keys(Id)
submit = browser.find_element_by_id("submit1").click()

wait1 = WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//div[@id = 'LoadingDiv']"))
)

status = browser.find_element_by_id("QuestionTitle").get_attribute("alt")
#print(status)
if status == None:
    #print("flag")
    browser.quit()
    print("不需要答题！")
    exit()

wait2 = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id = 'answer' and @value = '1']"))
)
total = browser.find_element_by_id("totalCount").get_attribute("value")

#print(total)

for i in range(0, int(total)):
    rightAnswer = browser.find_element_by_id("rightAnswer").get_attribute("value")
    print(rightAnswer)
    if rightAnswer == '1': 
        choose = browser.find_element_by_xpath("//input[@name = 'answer'][@value = '1']").click()
    else:
        choose = browser.find_element_by_xpath("//input[@name = 'answer'][@value = '2']").click()
        
    browser.find_element_by_id("submit2").click()
    print("done:", i)
    browser.implicitly_wait(3)
    wait = WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//div[@id = 'loadingDiv2']"))
    )



browser.quit()

