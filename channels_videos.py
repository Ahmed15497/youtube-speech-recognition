from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

channel_name = input('Enter the channel name: ')

driverPath = ChromeDriverManager().install()
driver = webdriver.Chrome(driverPath)
url = f'https://www.youtube.com/{channel_name}/videos'

driver.get(url)

height = driver.execute_script("return document.documentElement.scrollHeight")
previousHeight = -1

while previousHeight < height:
    previousHeight = height
    driver.execute_script(f'window.scrollTo(0,{height + 10000})')
    time.sleep(1)
    height = driver.execute_script("return document.documentElement.scrollHeight")

vidElements = driver.find_elements_by_id('thumbnail')
vid_urls = []
for v in vidElements:
    vid_urls.append(v.get_attribute('href'))
    
vid_urls = list(filter(None, vid_urls)) 
vid_urls = list(map(lambda x: x.split("v=",1)[1], vid_urls))

with open(f'{channel_name}_videosIDs.txt', 'w') as f:
    for item in vid_urls:
        f.write("%s\n" % item)


