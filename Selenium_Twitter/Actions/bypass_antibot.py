from Selenium_Twitter.helpers import wait_between, TypeInField, element_exists

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class BypassAntibot:
    def __init__(self, driver, action, configuration):
        self.driver = driver
        self.actions = action
        self.configuration = configuration
        self.tweet_xpath = '//div[@data-testid="tweetTextarea_0"]'
        self.tweet_button_xpath = '//div[@data-testid="tweetButton"]'
    
    def tweet(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://twitter.com/compose/tweet")
        tweet_el = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.tweet_xpath)))
        self.actions.move_to_element(tweet_el).click(tweet_el).perform()
        TypeInField(self.driver, self.tweet_xpath, 'Premier test')
        tweet_button_el = self.driver.find_element_by_xpath(self.tweet_button_xpath)
        self.actions.move_to_element(tweet_button_el).click(tweet_button_el).perform()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def newtab(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://twitter.com/compose/tweet")
        self.driver.switch_to.window(self.driver.window_handles[0])
        