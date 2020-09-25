import time;
from selenium import webdriver;

#time to refresh page
Timer = 120 #(120 seconds)

#youtube Link
link = https://www.youtube.com/watch?v=KC-4H23ztHg

#number of views
views = 5

driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
tine.sleep(Timer)
driver refresh()
