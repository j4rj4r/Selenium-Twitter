import os
import logging

from Selenium_Twitter.helpers import Helpers, header
import Selenium_Twitter.constants as const

from Selenium_Twitter.driver import Driver
from Selenium_Twitter.bot import Bot
    
def main():
    const.init()
    helpers = Helpers()
    # Load all configuration variables
    config = helpers.load_configuration(const.CONFIGURATION_FILE)
    # Configuration of the logging library
    helpers.logging_configuration()
    # Display header
    header()
    logging.info('Starting bot ...')

    username = profile = config['account']['username']
    profile = f'prof_{profile}'
    
    logging.info(f'Username : {username}')

    # Initialize driver and actions
    init_driver = Driver(profile)
    driver, action = init_driver.setup()

    bot = Bot(driver, action, config)

    # We check if the profile exists
    if not os.path.exists(f'./Profiles/{profile}'):
        url = 'https://twitter.com/i/flow/login'
        new = True
    else :
        url = 'https://twitter.com/home'
        new = False

    # Start bot actions
    test = bot.run(url, new)

if __name__ == "__main__":
    main()