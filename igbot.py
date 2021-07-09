from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="C:/Users/User/Desktop/geckodriver-v0.27.0-win64/geckodriver.exe")

    def login(self):
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
        self.comment_on()

    @staticmethod
    def be_like_human(comment, writeable_area):
        for letter in comment:
            writeable_area.send_keys(letter)
            time.sleep(random.randint(1,5)/30)

    def comment_on(self):
        driver = self.driver
        driver.get("https://www.instagram.com/p/CFSGUrOl4Ll/?utm_source=ig_web_copy_link")
        try:
            while True:
                possible_comments = ["tentando dnv", "esse up vai ser meu", "foda!", "quero dms!", "ahoo boa, garoto!", "vamo que vamo!", "que sonho, véi!", "tamo aqui na lida ksksk", 
                "nao desisto ate conseguir", "no pain no gain, carai kkk", "vamo na fe", "rambooora mlakada", "esse Up é MEEU! KKK", 
                "ainda nao desisti kkkkkk", "maaaano esse up ta mt lindo pqp", "adoro um Up,  e esse tá lindo", "que vontade de dar umas acelerada kkkk"]
                driver.find_element_by_class_name('Ypffh').click()
                comment_box = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(2,5))
                self.be_like_human(random.choice(possible_comments),comment_box)
                time.sleep(random.randint(30,40))
                driver.find_element_by_xpath("//button[contains(text(),'Post')]").click()
                time.sleep(5)
        except Exception as e:
            print("oh no! something went wrong! look at that: " + e)
            time.sleep(5)

BotClass = InstaBot('merryweather553', 'batata123')
BotClass.login()