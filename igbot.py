from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

print("!! IMPORTANT NOTICE !!")
print("This software is offered 'as-is', without any confirmation or validation ")
print("no harm will result in using it. With that said, I guarantee no data entered ")
print("by you, the user, in this program is stored, shared or sent externally.")
print("\nTHIS IS A MERE PROOF OF CONCEPT/WEEKEND PROJECT. Enjoy :D\n")

username = input("Type your account username: ")
password = input("Type your account' password (NO DATA WILL BE COLLECTED/SENT/STORED EXTERNALLY): ")
PATH = input("Type the full path to your Geckodriver.exe file: ")
hashtag = input("Type which hashtag you want the bot to comment on: #")

class InstaBot:
    def __init__(self, username, password, PATH, hashtag):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=PATH)
        self.hashtag = hashtag

    def login_action(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        fill_username = driver.find_element_by_xpath("//input[@name='username']")
        fill_username.click()
        fill_username.clear()
        fill_username.send_keys(self.username)
        fill_password = driver.find_element_by_xpath("//input[@name='password']")
        fill_password.click()
        fill_password.clear()
        fill_password.send_keys(self.password)
        fill_password.send_keys(Keys.RETURN)
        time.sleep(2)
        self.comment_action(hashtag)

    @staticmethod
    def set_random_typing_time(comment, writeable_area):
        for letter in comment:
            writeable_area.send_keys(letter)
            time.sleep(random.randint(1,32)/30)

    def comment_action(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        while True:
            for i in range(1, 4):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
            hrefs = driver.find_elements_by_tag_name("a")
            posts_hrefs = [elem.get_attribute("href") for elem in hrefs]
            [href for href in posts_hrefs if hashtag in href]
            print("found " + str(len(posts_hrefs)) + " photos in " + hashtag)

            for pic_href in posts_hrefs:
                driver.get(pic_href)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                try:
                    comments = ["hey, check my profile", "follow me and I'll follow you", 
                    "like my pics", "heyy"] #you can add as many comments as you want here, just follow the structure
                    driver.find_element_by_class_name('Ypffh').click()
                    comment_box = driver.find_element_by_class_name('Ypffh')
                    time.sleep(random.randint(2,5))
                    self.set_random_typing_time(random.choice(comments),comment_box)
                    time.sleep(random.randint(10,15))
                    driver.find_element_by_xpath("//button[contains(text(),'Post')]").click()
                    time.sleep(3.2)

                except Exception as e:
                    print("oh no! something went wrong! look at that: " + e)
                    time.sleep(5)

BotClass = InstaBot(username, password, PATH, hashtag)
BotClass.login_action()