from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from icecream import ic
from dotenv import load_dotenv
import os

load_dotenv()

SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/"
TWITTER_USERNAME = os.environ["TWITTER_USER"]
TWITTER_PASS = os.environ["TWITTER_PASS"]
ISP_NAME = "Google Fiber"
ISP_USERNAME = "googlefiber"
PROMISED_UP = 200
PROMISED_DOWN = 200


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        url = SPEED_TEST_URL
        self.driver.get(url)
        sleep(3)
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        sleep(40)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                       '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div['
                                                       '2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                     '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        ic(self.down)
        ic(self.up)
        return self.down, self.up

    def tweet_at_provider(self):
        url = TWITTER_URL
        self.driver.get(url)
        sleep(5)

        # Sign-In
        sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span')
        ic(sign_in.text)
        sign_in.click()
        sleep(10)
        username = self.driver.find_element(By.NAME, "text")
        username.send_keys(TWITTER_USERNAME)
        sleep(5)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                   '2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        next_button.click()
        sleep(10)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PASS)
        sleep(5)
        login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        login.click()
        sleep(30)
        # Manually Enter Auth Code

        # Generate Message
        test_tweet = "testing my bot"
        ic(test_tweet)
        tweet = f"Hey {ISP_NAME}, why is my internet speed {self.down}down/{self.up}ip when I pay for " \
                f"{PROMISED_DOWN}down/{PROMISED_UP}up?"
        ic(tweet)



        #Create a Tweet
        # draft_post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span')
        # ic(draft_post.text)
        # draft_post.click()
        # sleep(5)
        # draft_tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
        #                                              '2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span')
        draft_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div')
        ic(draft_tweet.text)
        draft_tweet.send_keys(test_tweet)
        sleep(5)

        #Post Tweet
        post_tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/span/span')
        ic(post_tweet.text)
        post_tweet.click()



