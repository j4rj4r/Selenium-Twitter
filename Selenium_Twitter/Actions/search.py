from random import shuffle
import logging

from Selenium_Twitter.helpers import TypeInField

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class Search:
    def __init__(self, driver, action, configuration):
        self.driver = driver
        self.actions = action
        self.configuration = configuration
        self.search_xpath = '//input[@data-testid="SearchBox_Search_Input"]'
        self.latest_xpath = '//span[contains(text(), "Récent")]'
        self.clearsearch_xpath = '//div[@data-testid="clearButton"]'

    def first_search(self):
        shuffle(self.configuration['WordsToSearch'])
        wordlist = self.configuration['WordsToSearch']
        keyword = f'{wordlist[0]} min_retweets:{self.configuration["MinRetweet"]} -filter:replies lang:fr'
        logging.info(f'Search : {wordlist[0]}')
        search_el = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.search_xpath)))
        self.actions.move_to_element(search_el).click(search_el).perform()
        TypeInField(self.driver, self.search_xpath, keyword)
        search_el.send_keys(Keys.RETURN)

        latest_el = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.latest_xpath)))
        self.actions.move_to_element(latest_el).click(latest_el).perform()


    def search(self, word):
        search_el = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.search_xpath)))
        self.actions.move_to_element(search_el).click(search_el).perform()
        clear_el = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.clearsearch_xpath)))
        self.actions.move_to_element(clear_el).click(clear_el).perform()

        keyword = f'{word} min_retweets:{self.configuration["MinRetweet"]} -filter:replies lang:fr'
        TypeInField(self.driver, self.search_xpath, keyword)
        search_el.send_keys(Keys.RETURN)

        latest_el = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.latest_xpath)))
        self.actions.move_to_element(latest_el).click(latest_el).perform()