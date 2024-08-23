from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = ""

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://twitter.com/BarackObama')
time.sleep(2)

tweet_height = 700

tweets_collected = []
for i in range(10):
    driver.execute_script(f"window.scrollBy(0, {tweet_height});")
    time.sleep(2)

    tweets = driver.find_elements(By.XPATH, '//article//div[@data-testid="tweetText"]')
    dates = driver.find_elements(By.XPATH, '//article//time')

    for tweet, date in zip(tweets, dates):
        tweet_text = tweet.text
        tweet_date = date.get_attribute("datetime")
        if tweet_text not in tweets_collected:
            tweets_collected.append(tweet_text)
            print(f"Tweet {len(tweets_collected)} ({tweet_date}):\n{tweet_text}\n{'-'*50}\n")

driver.quit()
