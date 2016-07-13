
# coding: utf-8

# In[1]:

import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


# In[9]:

#This tests the function on a single appid. I am having trouble making the login function global.

appid=str(881214611)
def scrape(ID):
    driver=login()
    
    url= "https://sensortower.com/ios/us/_/app/_/" + ID
    sleep(5)
    driver.get(url)
    
    name = driver.find_element_by_css_selector('.app-name-wrapper')
    pub = driver.find_element_by_css_selector('.publisher-item a')
    dl = driver.find_element_by_css_selector(".downloads") 
    rev = driver.find_element_by_css_selector('.revenue')
    fivestar_count = driver.find_element_by_css_selector('tr:nth-child(1) .rating-count')
    fourstar_count = driver.find_element_by_css_selector('tr:nth-child(2) .rating-count')
    threestar_count = driver.find_element_by_css_selector('tr:nth-child(3) .rating-count')
    twostar_count = driver.find_element_by_css_selector('tr:nth-child(4) .rating-count')
    onestar_count = driver.find_element_by_css_selector('tr:nth-child(5) .rating-count')
    
    appname = name.text
    publisher = pub.text
    downloads = dl.text
    revenue = rev.text
    fivecount = fivestar_count.text
    fourcount = fourstar_count.text
    threecount = threestar_count.text
    twocount = twostar_count.text
    onecount = onestar_count.text
    
    with open('test.csv','w',newline='') as csvfile:
        writer=csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([appname,ID,publisher,downloads,revenue,fivecount,fourcount,threecount,twocount,onecount])


# In[ ]:




# In[2]:

def login():
    driver = webdriver.Firefox()
    driver.get("http://www.sensortower.com")
    sleep(6)
    login = driver.find_element_by_class_name("nav-item-login")
    login.click()
    sleep(3)
    elem1 = driver.find_element_by_id('user_email')
    elem1.clear()
    elem1.send_keys('vivian.gao.17@dartmouth.edu')
    
    remember = driver.find_element_by_name('user[remember_me]')
    remember.click()
    
    elem2 = driver.find_element_by_id('user_password')
    elem2.clear()
    elem2.send_keys('goodluck' + Keys.ENTER)
    sleep(5)
    return driver
    #assert "No results found." not in driver.page_source
    #driver.close()
    


# In[5]:




# In[4]:




# In[ ]:




# In[ ]:




# In[11]:

#only need to use this once
with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['name','appid','publisher','downloads','revenue','fivecount','fourcount','threecount','twocount',
                     'onecount'])
    


# In[ ]:



