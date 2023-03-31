from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import csv

data_list=[]
chrome_options =webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())

chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("user-data-dir=C:/Users/Dell/AppData/Local/Google/Chrome/User Data")

driver = webdriver.Chrome(service=s,options=chrome_options)
wait=WebDriverWait(driver, 60)

url='https://www.flak.no/login'
driver.get(url)


login=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type='submit']")))
login=driver.find_element(By.XPATH,"//input[@type='submit']").click()
# driver.execute_script("arguments[0].click();", login)

time.sleep(5)


url='https://www.flak.no/produkter/baatpleie-og-opplagsutstyr/vask-pleie-og-vedlikehold/respect-2x-nano-protect-250-ml-p1080645'
# url='https://www.flak.no/produkter/?ProdNo=1034423'
driver.get(url)


# title=driver.find_element(By.XPATH,"//div[contains(@class,'productPageItem prod_mainwrapper topfail')]/div[1]")
# title=title.text.split('\n')[0]
# print(title)
title = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'productPageItem prod_mainwrapper topfail')]/div[1]")))

try:
        product_title = driver.find_element(By.XPATH,"//div[contains(@class,'productPageItem prod_mainwrapper topfail')]/div[1]").text
        
except:
        product_title = " "
        pass

try:
        small_desc_1 = driver.find_element(By.XPATH,"//div[@class='prod_notenm_full']/h2").text
        small_desc_2 = driver.find_element(By.XPATH,"//div[@class='prod_notenm_full']/*[2]").text
        full_descript = small_desc_1 + " " + small_desc_2
except:
        full_descript= " "
        pass

try:
        long_desc_1 = driver.find_element(By.XPATH,"//div[@class='prod_notenm_full']/katalog").text
        # long_desc_2 = driver.find_element(By.XPATH,"//div[@class='prod_notenm_full']/katalog/font/*[2]").text
        full_decrip = long_desc_1 
except:
        full_decrip = " "
        pass

try:
        product_number = driver.find_element(By.XPATH,"//div[@class='prod_header_container']/div/dl/dd[1]").text
        print(product_number)
except:
        product_number = " "
        pass

try:
        original_number = driver.find_element(By.XPATH,"//div[@class='prod_headerinfo']/dl/*[4]").text
except:
        original_number = " "
        pass

try:
        unit_pacakage_perunit = driver.find_element(By.XPATH,"//div[@class='prod_header_container']/div/dl/dd[5]").text
        print(unit_pacakage_perunit)
except:
        unit_pacakage_perunit = " "
        pass

try:
        storage = driver.find_element(By.XPATH,"//div[@class='prod_header_container']/div/dl/dd[9]").text
        print(storage)
except:
        storage = " "
        pass

try:
        price_v = driver.find_element(By.XPATH,"//div[@class='price']").text
        print(price_v)
except:
        price_v = " "
        pass

try:
        recomended_price = driver.find_element(By.XPATH,"//div[@class='prod_header_container']/div/dl/dd[6]").text
        print(recomended_price)
except:
        recomended_price = " "
        pass
try:
        Strekkode = driver.find_element(By.XPATH,"//div[@class='prod_headerinfo']/dl/*[6]").text
        print(Strekkode)
except:
        Strekkode = " "
        pass
        
# text_=driver.find_element(By.XPATH,"//div[@class='prod_headerinfo']/dl")
# print(text_.text)

# data_main=text_.text.split('\n')
# index=0
# while(index<len(data_main)/2):
#     print(data_main[index])
#     data=data_main[index+1]
#     print(data)
#     index+=2

# description=driver.find_element(By.XPATH,"//div[@class='prod_notenm_full']").text
# print(description)

# price=driver.find_element(By.XPATH,"//div[@class='addToCartWrapper']//div[@class='price']").text
# print(price)

category=driver.find_element(By.XPATH,"//li[@class='level-2 productCategory']").text
print(category)

subcategory=driver.find_element(By.XPATH,"//li[@class='level-3 productCategory']").text
print(subcategory)

product=driver.find_element(By.XPATH,"//li[@class='level-4 productCategory']").text
print(product)

# try:
# time.sleep(200)
# width=driver.find_element(By.XPATH,"//div[@class='prod_notenm_full']/br[1]/following-sibling::text()[1]")
# print("width")
# print(width)
# element = driver.find_element(By.XPATH,"//div[@class='prod_notenm_full']")
# text = element.find_element(By.TAG_NAME,'br')
# print(text.get_attribute("textContent").strip())

# external_thread = driver.find_element(By.XPATH,"//div[@class='prod_notenm_full']/*[9]").text
# thread_length = driver.find_element(By.XPATH,"//div[@class='prod_notenm_full']/*[11]").text
# transmitter_system = driver.find_element(By.XPATH,"//div[@class='prod_notenm_full']/*[13]").text
# specification = [text,external_thread,thread_length,transmitter_system]

# except:
#         specification = []
#         pass

# try:
#         lexus = driver.find_element(By.XPATH,"//div[@class='prod_notenm_full']/*[18]").text
#         mercury = driver.find_element(By.XPATH,"//div[@class='prod_notenm_full']/*[20]").text
#         nissan = driver.find_element(By.XPATH,"//div[@class='prod_notenm_full']/*[22]").text
#         toyota = driver.find_element(By.XPATH,"//div[@class='prod_notenm_full']/*[24]").text
#         yamaha = driver.find_element(By.XPATH,"//div[@class='prod_notenm_full']/*[26]").text
#         oe_number = [lexus,mercury,nissan,toyota,yamaha]
# except:
#         oe_number=[]
#         pass

# # Close the driver

try:
    image_url1=driver.find_element(By.XPATH,"//div[@class='sliding_product prodMainImg']/img[1]").get_attribute('src')
    print(image_url1)
except:
        image_url1=" "
        pass

try:
    image_url2=driver.find_element(By.XPATH,"//div[@id='slidingProduct1034423']/img[2]").get_attribute('src')
    print(image_url2)
except:
        image_url2=" "
        pass
try:
    image_url3=driver.find_element(By.XPATH,"//div[@id='slidingProduct1034423']/img[3]").get_attribute('src')
    print(image_url3)
except:
        image_url3=" "
        pass
try:
    image_url4=driver.find_element(By.XPATH,"//div[@id='slidingProduct1034423']/img[4]").get_attribute('src')
    print(image_url4)
except:
        image_url4=" "
        pass
try:
    image_url5=driver.find_element(By.XPATH,"//div[@id='slidingProduct1034423']/img[5]").get_attribute('src')
    print(image_url1)
except:
        image_url5=" "
        pass
try:
    image_url6=driver.find_element(By.XPATH,"//div[@id='slidingProduct1034423']/img[6]").get_attribute('src')
    print(image_url6)
except:
        image_url6=" "
        pass
try:
        lexus = driver.find_element(By.XPATH,"//div[@class='prod_notenm_full']").text
        lexus1=lexus.split('\n')
        index_spec=lexus1.index("Spesifikasjoner:")
        index_oe_num=lexus1.index("OE-nummer:")
        specification=lexus1[index_spec+1:index_oe_num]
        print(specification)
except:
       specification=""
try:
        oe_number=lexus1[index_oe_num+1:]
        print(oe_number)
except:
       oe_number=" "
       pass

with open('flak.csv', 'a', encoding='utf-8', newline='') as f_object:
    headers=['product_title','full_descript','full_decrip','product_number','original_number','unit_pacakage_perunit','storage,price_v',
            'recomended_price','specification','oe_number','Strekkode','category','subcategory','product','image_url1','image_url2','image_url3','image_url4','image_url5','image_url6']
    writer_object = csv.writer(f_object)
    writer_object.writerow(headers)
    writer_object.writerow(
        [product_title,full_descript,product_number,original_number,unit_pacakage_perunit,storage,price_v,
            recomended_price,specification,oe_number,Strekkode,category,subcategory,product,image_url1,image_url2,image_url3,image_url4,image_url5,image_url6])
    f_object.close()
driver.quit()