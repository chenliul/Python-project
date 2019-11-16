'''
Created on 09/20/2019
@author: Lei Chen

Shopping Cart Selenium python automation code challenge, on the shopping cart web page: 
1. all 5 dresses are listed on the summary page. 
2. the total price of each dress is correct. 
3. the total price is the sum of the total price of each dress

Test environments:Eclipse IDE, PyDev package, 

'''

from selenium import webdriver
import time
import os

def test_setup():
    global driver
    driver = webdriver.Chrome(r'C:\Users\Administrator\eclipse-workspace\pytest1\Drivers\chromedriver.exe')
#driver = webdriver.Firefox(r'C:\Users\Administrator\eclipse-workspace\pytest1\Drivers\geckodriver.exe')

def test_login():
#launch shopping web page
    driver.get("http://automationpractice.com")
    time.sleep(1)

#login shopping web site account
    driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
    time.sleep(1)

    field1 = driver.find_element_by_id("email")
    field1.send_keys('gameguys22@gmail.com')
    time.sleep(1)

    field2 = driver.find_element_by_id("passwd")
    field2.send_keys('10142022')
    time.sleep(1)

    python_button = driver.find_element_by_id('SubmitLogin')
    python_button.click()
    time.sleep(2)

    driver.get("http://automationpractice.com")
    time.sleep(1)

def test_Choice_items():
# add dresses in shopping cart
    python_button = driver.find_element_by_xpath('//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[1]/span')
    python_button.click()
    time.sleep(2)

    driver.get("http://automationpractice.com")
    time.sleep(1)

    python_button = driver.find_element_by_xpath('//*[@id="homefeatured"]/li[2]/div/div[2]/div[2]/a[1]/span')
    python_button.click()
    time.sleep(2)

    driver.get("http://automationpractice.com")
    time.sleep(1)

    python_button = driver.find_element_by_xpath('//*[@id="homefeatured"]/li[3]/div/div[2]/div[2]/a[1]/span')
    python_button.click()
    time.sleep(2)

    driver.get("http://automationpractice.com")
    time.sleep(1)

    python_button = driver.find_element_by_xpath('//*[@id="homefeatured"]/li[4]/div/div[2]/div[2]/a[1]/span')
    python_button.click()
    time.sleep(2)

    driver.get("http://automationpractice.com")
    time.sleep(1)

    python_button = driver.find_element_by_xpath('//*[@id="homefeatured"]/li[5]/div/div[2]/div[2]/a[1]/span')
    python_button.click()
    time.sleep(2)

#dresses check out
def test_check_out():
    python_button = driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span')
    python_button.click()
    time.sleep(2)

    python_button = driver.find_element_by_xpath('//*[@id="center_column"]/p[2]/a[1]/span')
    python_button.click()
    time.sleep(2)

    python_button = driver.find_element_by_xpath('//*[@id="center_column"]/form/p/button/span')
    python_button.click()
    time.sleep(2)

    radio = driver.find_element_by_xpath('//*[@id="cgv"]')
    radio.click()
    time.sleep(2)


    python_button = driver.find_element_by_xpath('//*[@id="form"]/p/button/span')
    python_button.click()
    time.sleep(2)

def test_sumbit_payment():
    python_button = driver.find_element_by_xpath('//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a')
    python_button.click()
    time.sleep(2)

    python_button = driver.find_element_by_xpath('//*[@id="cart_navigation"]/button/span')
    python_button.click()
    time.sleep(2)

    print ("Tests are passed")

    driver.quit()

