from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

SIMILAR_ACCOUNT = "leomessi"
USERNAME = "rafetcode@gmail.com"
PASSWORD = "secret"


class InstaFollower:

    def __init__(self):

        self.options =webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)

    def login(self):

        self.driver.get(url="https://www.instagram.com/accounts/login/")
        username_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        username_input.send_keys(f"{USERNAME}")
        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        password_input.send_keys(f"{PASSWORD}", Keys.ENTER)

    def find_followers(self):

        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(5.2)

    def follow(self):
        time.sleep(5.2)
        for i in range(1, 50):
            follow_button = self.driver.find_element(By.CSS_SELECTOR, value=f"body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(2) > div > div:nth-child({i}) > div > div > div > div:nth-child(3) > div > button")
            follow_button.click()


insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()


