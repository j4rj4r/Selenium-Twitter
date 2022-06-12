from random import shuffle
import logging

from Selenium_Twitter.Actions.search import Search
from Selenium_Twitter.Actions.get_tweet import Get_tweet
from Selenium_Twitter.helpers import wait_between, TypeInField, element_exists

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class Bot:
    def __init__(self, driver, action, configuration):
        self.driver = driver
        self.actions = action
        self.configuration = configuration
        self.email_xpath = '//input[@autocomplete="username"]'
        self.password_xpath = '//input[@autocomplete="current-password"]'
    
    def login(self):
        email_el = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.email_xpath)))
        self.actions.move_to_element(email_el).click(email_el).perform()
        TypeInField(self.driver, self.email_xpath, self.configuration['account']['username'])
        email_el.send_keys(Keys.RETURN)

        password_el = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.password_xpath)))
        self.actions.move_to_element(password_el).click(password_el).perform()
        TypeInField(self.driver, self.password_xpath, self.configuration['account']['password'])
        password_el.send_keys(Keys.RETURN)

    def run(self, url, new):
        sleeptime = self.configuration['TimeBetweenSearch']
        self.driver.get(url)
        if new:
            self.login()
        else :
            # We check that we are well connected
            if element_exists('//input[@autocomplete="username"]', self.driver) :
                self.login()
        
        logging.info('Logged in')

        if element_exists('//span[contains(text(), "Accepter tous les cookies")]', self.driver):
            cookie_el = self.driver.find_element(by=By.XPATH, value='//span[contains(text(), "Accepter tous les cookies")]')
            self.actions.move_to_element(cookie_el).click(cookie_el).perform()
            logging.info('Cookies accepted')

        search = Search(self.driver, self.actions, self.configuration)
        search.first_search()

        tweet_action = Get_tweet(self.driver, self.actions, self.configuration)
        tweet_action.get_tweet()

        wait_between(sleeptime, sleeptime)
        
        while True : 
            shuffle(self.configuration['WordsToSearch'])
            for word in self.configuration['WordsToSearch']:
                logging.info(f'Search : {word}')
                search.search(word)
                tweet_action.get_tweet()
                wait_between(sleeptime, sleeptime)