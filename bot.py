from selenium import webdriver
from getpass import getpass

user = input('Enter your username: ')
password = getpass('Enter your password : ')

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')

username_box = driver.find_element_by_id('email')
username_box.send_keys(user)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(password)

login_btn = driver.find_element_by_id('u_0_2')
login_btn.submit()
