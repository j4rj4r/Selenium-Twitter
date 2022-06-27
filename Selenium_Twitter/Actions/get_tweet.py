from random import shuffle
import logging

from Selenium_Twitter.helpers import wait_between, element_exists

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class Get_tweet:
    def __init__(self, driver, action, configuration):
        self.driver = driver
        self.actions = action
        self.configuration = configuration
        self.pagecard_xpath = '//article[@data-testid="tweet"]'
    
    def get_data(self, card):
        """Extract data from tweet card"""
        data = {}
        try:
            username = card.find_element(by=By.XPATH, value='.//span').text
            data['username_el'] = card.find_element(by=By.XPATH, value='.//span')
            data['username'] = username
        except:
            return None

        try:
            arobaseusername = card.find_element(by=By.XPATH, value='.//span[contains(text(), "@")]').text
            data['arobaseusername'] = arobaseusername
        except:
            return None

        try:
            id = card.find_element(by=By.XPATH, value='.//img[contains(@src, "https://pbs.twimg.com/profile_images/")]')
            user_id = id.get_attribute('src').split('/')[4]
            data['user_id'] = user_id
        except:
            return None


        try:
            postdate = card.find_element(by=By.XPATH, value='.//time').get_attribute('datetime')
            data['postdate'] = postdate
        except:
            data['postdate'] = ""

        try:
            text = card.find_element(by=By.XPATH, value='.//div[@data-testid="tweetText"]').text
            data['text'] = text
        except:
            data['text'] =  ""

        try:
            reply_cnt = card.find_element(by=By.XPATH, value='.//div[@data-testid="reply"]').text
            data['reply_cnt'] = reply_cnt
        except:
            data['reply_cnt'] = "0"

        try:
            retweet_cnt = card.find_element(by=By.XPATH, value='.//div[@data-testid="retweet"]').text
            data['retweet_el'] = card.find_element(by=By.XPATH, value='.//div[@data-testid="retweet"]')
            data['retweet_cnt'] = retweet_cnt
        except:
            retweet_cnt = card.find_element(by=By.XPATH, value='.//div[@data-testid="unretweet"]').text
            data['retweet_cnt'] = retweet_cnt
            data['retweet_el'] = None

        try:
            like_cnt = card.find_element(by=By.XPATH, value='.//div[@data-testid="like"]').text
            data['like_el'] = card.find_element(by=By.XPATH, value='.//div[@data-testid="like"]')
            data['like_cnt'] = like_cnt
        except:
            like_cnt = card.find_element(by=By.XPATH, value='.//div[@data-testid="unlike"]').text
            data['like_cnt'] = like_cnt
            data['like_el'] = None
        try:
            element = card.find_element(by=By.XPATH, value='.//a[contains(@href, "/status/")]')
            tweet_url = element.get_attribute('href')
            data['tweet_url'] = tweet_url
        except:
            return None

        return data

    def get_tweet(self):
        WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((By.XPATH, self.pagecard_xpath)))
        page_cards = self.driver.find_elements(by=By.XPATH, value=self.pagecard_xpath)
        for card in page_cards:
            data_card = self.get_data(card)
            print(data_card)
            if data_card and data_card != None:
                if data_card['like_el'] != None and data_card['retweet_el'] != None :
                    if not any(user in data_card['arobaseusername'] for user in self.configuration['BlacklistAccounts']): 
                        if data_card['like_el'] != None :
                            if self.configuration["AutoLike"] :
                                like_el = data_card['like_el']
                                self.actions.move_to_element(like_el).click(like_el).perform()
                                logging.info('Retweeted')
                                wait_between(0.2, 0.5)
                        if data_card['retweet_el'] != None :
                            if self.configuration["AutoRetweet"] :
                                retweet_el = data_card['retweet_el']
                                self.actions.move_to_element(retweet_el).click(retweet_el).perform()
                                retweet_confirm_el = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//div[@data-testid="retweetConfirm"]')))
                                self.actions.move_to_element(retweet_confirm_el).click(retweet_confirm_el).perform()
                                logging.info('Liked')
                                wait_between(0.2, 0.5)
                        if self.configuration["AutoFollow"] :
                            username_el = data_card['username_el']
                            self.actions.move_to_element(username_el).perform()
                            try :
                                card_hover = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af')))
                            except :
                                pass
                            # Find the follow button
                            if element_exists('.//span[contains(text(), "Suivre")]', card_hover, by=By.XPATH) :
                                follow_el = card_hover.find_element(by=By.XPATH, value='.//span[contains(text(), "Suivre")]')
                                self.actions.move_to_element(follow_el).click(follow_el).perform()
                                logging.info('Followed')