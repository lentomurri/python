#! python3

#The program gets the keywords from the command line, request the related search page and will open the first four links

import sys, webbrowser
from selenium import webdriver

# TODO create string by joining the sys.argv
string = " ".join(sys.argv[1:])

# avoid selenium opening page
op = webdriver.ChromeOptions()
op.add_argument('headless')


driver = webdriver.Chrome(r"C:\Users\Lento\Downloads\chromedriver_win32 (1)\chromedriver.exe", options=op) # assign the location of the chromedriver
driver.get("https://www.google.com/search?q=" + string) # searches for google page related to the string

links = driver.find_elements_by_xpath("//*[@class='r']/a") # searches for link elements direct children of class r

# opens first 4 links
for link in links[:4]:
    webbrowser.open(link.get_attribute("href"))
