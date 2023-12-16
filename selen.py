from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import csv
price=[]
fields = ['title', 'price', 'image', 'newpage']  
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
os.environ['PATH']+=r"C:\seleniumdriver\chromedriver-win64"
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/s?k=water+bottle&crid=2CIPBRW1IT7FX&sprefix=wat%2Caps%2C1389&ref=nb_sb_ss_ts-doa-p_2_3")
isnextdisabled=False
while not isnextdisabled:
    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,'//div[@data-component-type="s-search-result"]')))
    elemlist=driver.find_element(By.CSS_SELECTOR,"div.s-main-slot.s-result-list.s-search-results.sg-row")
    items=elemlist.find_elements(By.XPATH,'//div[@data-component-type="s-search-result"]')
    for item in items:
        try:
            title=[]
            title.append(item.find_element(By.TAG_NAME,'h2').text)
            title.append(item.find_element(By.CSS_SELECTOR,'.a-price').text.replace("\n"," "))
            title.append(item.find_element(By.CSS_SELECTOR,'.s-image').get_attribute("src"))
            title.append(item.find_element(By.CSS_SELECTOR,'.a-link-normal').get_attribute('href'))
            price.append(title)
        except:
            print("some error")
    try:
        nextbtn=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'s-pagination-next')))
        next_class=nextbtn.get_attribute('class')
        if 'disabled' in next_class:
            isnextdisabled=True
            break
        else:
            driver.find_element(By.CLASS_NAME,'s-pagination-next').click()
    except Exception as e:
        isnextdisabled=True
with open("file1.csv", 'w',newline='',encoding='utf-8') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(price) 