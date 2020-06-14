# web_automated_ML_data_collector
This project was developed to automatically download image data sets from the web for my ML projects.

## Inspiration:

Making machine learning models requires a lot of data, often we have to collect data from the web. But wait a minute why should a ML enthusiast need to waste time downloading images from the web...

## Set up
This project requires prior installation of selenium, ChromeDriver and python 3.0+.
Get Chrome driver from here [Choose the win32.zip for windows users] :
https://chromedriver.storage.googleapis.com/index.html?path=81.0.4044.138/

Important: The chrome driver works with Chrome browser version 81. As of June 14, 2020 the latest version is 83 and Google hates it when you use an older version. {It will upgrade all versions automatically}
To solve this, I have attached a Google Chrome version 81 installation file and once it is installed go to:
C:\Program Files (x86)\Google\Update and rename the "update" folder to something else.
This will disable auto-updates and save you some future headaches.


## About the code
1) The code uses the enhanced ability of selenium python. 
2) By default the code returns the dataset of 'Dogs', however by changing line 8: "topic = 'Dogs'", you can get the topic you like.
3) The code uses the chromium web driver
4) The code opens the google search engine, types in the topic of interest and navigates through "Images" tab
5) It then downloads all the images in the page and saves them to a folder named 'topic' [i.e. whatever topic you choose ]
4) Modify the code to suite your own needs and have fun :)
