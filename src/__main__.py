#Importing packages
from selenium import webdriver
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

driver.get('https://forums.edmunds.com/discussion/40920/ford/f-150/fuel-economy-test-2-7-liter-ecoboost-vs-5-0-liter-v8-2015-ford-f-150-long-term-road-test')

comments = pd.DataFrame(columns=['Date', 'user_id', 'comments'])
ids = driver.find_elements_by_xpath("//*[contains(@id,'Comment_')]")
comment_ids = []
for i in ids:
    comment_ids.append(i.get_attribute('id'))

for x in comment_ids:
    # Extract dates from for each user on a page
    user_date = driver.find_elements_by_xpath('//*[@id="' + x + '"]/div/div[2]/div[2]/span[1]/a/time')[0]
    date = user_date.get_attribute('title')

    # Extract user ids from each user on a page
    userid_element = driver.find_elements_by_xpath('//*[@id="' + x + '"]/div/div[2]/div[1]/span[1]/a[2]')[0]
    userid = userid_element.text

    # Extract Message for each user on a page
    user_message = driver.find_elements_by_xpath('//*[@id="' + x + '"]/div/div[3]/div/div[1]')[0]
    comment = user_message.text

    # Adding date, userid and comment for each user in a dataframe
    comments.loc[len(comments)] = [date, userid, comment]
driver.save_screnshot('test.png')
driver.quit()
