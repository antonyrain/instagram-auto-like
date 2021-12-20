from auth import users_settings_dict
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time, random
import random


class Bot():
    def __init__(self, login, password, lang, user_agent, window_size):
        self.login = login
        self.password = password
        options = Options()

        # headless mode
        # options.headless = True
        #options.add_argument("--headless")
        # disable webdriver mode
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(f"--lang={lang}")
        options.add_argument(
            f"user-agent={user_agent}")
        # set proxy
        # options.add_argument("--proxy-server=198.50.163.192:3129")
        options.add_argument(f"--window-size={window_size}")
        self.browser = webdriver.Chrome(options=options)


    def close_browser(self):
        self.browser.close()
        self.browser.quit()


    def login_chrome(self):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(5, 7))
        # login = self.login
        # password = self.password
        print(login + '\n Authorization...')
        username_input = browser.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(login)
        time.sleep(random.randrange(5, 7))
        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(random.randrange(5, 7))
        password_input.send_keys(Keys.ENTER)


    def search_by_hashtag(self):
        print("Search by hashtag...")

        with open("hashtags_1.txt", "r", encoding="utf-8") as hashtags_list:
            word = hashtags_list.read().split()
            hashtag = random.choice(word)

        browser = self.browser
        time.sleep(random.randrange(5, 10))
        browser.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
        time.sleep(random.randrange(5, 10))
        browser.find_element_by_class_name('v1Nh3').click()
        print("Likes: " + hashtag)

        for i in range(2):
            try:
                time.sleep(random.randrange(5, 10))
                browser.find_element_by_class_name('fr66n').click()
            except:
                pass
            time.sleep(random.randrange(5, 10))
            browser.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div/button/div').click()

        # browser.find_element_by_class_name('wpO6b').click()
        browser.find_element_by_xpath('/html/body/div[6]/div[3]/button/div').click()
        print("Successfully completed... \n" + login)
        time.sleep(random.randrange(5, 10))


for user, auth in users_settings_dict.items():
    login = auth["login"]
    password = auth["password"]
    lang = auth["lang"]
    user_agent = auth["user_agent"]
    window_size = auth["window_size"]



    bot1 = Bot(login, password, lang, user_agent, window_size)
    bot1.login_chrome()
    for i in range(2):
        bot1.search_by_hashtag()
    bot1.close_browser()
    #time.sleep(random.randrange(5, 10))
