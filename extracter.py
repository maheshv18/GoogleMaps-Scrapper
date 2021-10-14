

from selenium import webdriver
import pyautogui
from bs4 import BeautifulSoup
import threading
import time
import pandas as pd



print("Enter the filename")
filename = str(input())

browser = webdriver.Chrome("C:/Users/MaheshV/Downloads/chromedriver.exe")
record = []
e = []


def Selenium_extractor():
    time.sleep(2)
    a = browser.find_elements_by_class_name("VkpGBb")
    time.sleep(1)
    for i in range(len(a)):
        a[i].click()
        time.sleep(2)
        source = browser.page_source
        # Beautiful soup for scraping the html source
        soup = BeautifulSoup(source, 'html.parser')
        try:
            Name_Html = soup.findAll('div', {"class": "SPZz6b"})

            name = Name_Html[0].text
            if name not in e:
                e.append(name)
                print(name)
                Phone_Html = soup.findAll('span', {"class": "LrzXr zdqRlf kno-fv"})
                phone = Phone_Html[0].text
                print(phone)

                Address_Html = soup.findAll('span', {"class": "LrzXr"})

                address = Address_Html[0].text

                try:
                    Website_Html = soup.findAll('div', {"class": "QqG1Sd"})
                    web = Website_Html[0].findAll('a')

                    website = web[0].get('href')
                except:
                    website = "Not available"

                record.append((name, phone, address, website))
                df = pd.DataFrame(record,
                                  columns=['Name', 'Phone number', 'Address', 'Website'])
                df.to_csv(filename + '.csv', index=False, encoding='utf-8')

        except:
            print("error")
            continue

    try:
        time.sleep(1)
        next_button = browser.find_element_by_id("pnnext")
        next_button.click()
        browser.implicitly_wait(2)
        time.sleep(2)
        Selenium_extractor()
    except:
        print("ERROR occured at clicking net button")


print("Enter the link of the page")
link = input()
browser.get(str(link))
time.sleep(10)
Selenium_extractor()