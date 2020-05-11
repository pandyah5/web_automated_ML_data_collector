from selenium import webdriver
import urllib.request   # For python 2 just import urllib, urllib.request is needed for python 3+ because it has been been segmented into many subsets
from selenium.webdriver.common.keys import Keys   # Helps to stimulate keyboard key presses
import os   # For making directories to store images
import time

# EDIT THIS AS PER THE TYPE OF IMAGES YOU NEED
topic = 'Dogs'
#

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome("D:\Python files\Web Automation\chromedriver.exe")
print('Welcome to database and sample creator, this has been developed by Hetav Pandya to help you get databases for your ML Projects')

## Get Chrome driver from here:
# https://chromedriver.storage.googleapis.com/index.html?path=81.0.4044.138/
# Choose the win32.zip for windows users

driver.get('https://www.google.com/') # Put the URL you wanna go to
search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input') # Saves the Xpath to the variable search
search.send_keys(topic) # Sends text to the textbox

# Pressing the 'enter' key in the browser text box
search.send_keys(Keys.ENTER) # Do not forget to import Keys from Selenium - Line 4

driver.find_element_by_link_text('Images').click()

# Gets all the images on the web page
images = driver.find_elements_by_tag_name('img')
print(len(images), "Images Found")
print(images)
i = 1

# Creating a seperate folder for storing data
filePath = "D:\\Python files\\Web Automation\\" + topic
os.makedirs(filePath)
os.chdir(filePath)

time.sleep(5) # Optional

# Saving all the images found in the folder created
for image in range(1, len(images)):
    try:
        src = images[image].get_attribute('src')
        urllib.request.urlretrieve(src, "image" + str(i) + ".png")
        i += 1
    except:
        pass

driver.close()

## Notes:

# driver.save_screenshot("Home Page.png") - For screenshots
# For getting the xpath you need to search for the element in the source code and then press right click -> Copy -> Copy XPath/full XPath
