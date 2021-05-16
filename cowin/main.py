import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://selfregistration.cowin.gov.in/")

time.sleep(2)

mobileNumberInput = driver.find_element_by_id('mat-input-0')
mobileNumberInput.clear()

mobileNumberInput.send_keys('9265372319')

print('mobile number inserted...')
print('pls enter otp:')

getOTPBtn = driver.find_element_by_class_name('next-btn').click()

otp = int(input('pls enter otp:'))

otpInput = driver.find_element_by_id('mat-input-1')

otpInput.send_keys(otp)

verifyBtn = driver.find_element_by_class_name('next-btn').click()

driver.get('https://selfregistration.cowin.gov.in/appointment')

stateDropDOwn = driver.find_element_by_id('mat-select-28').click()

gujarat = driver.find_element_by_xpath(
    '/html/body/div[2]/div[2]/div/div/div/mat-option[12]/span')

print(gujarat)

print(otp)
# driver.close()
