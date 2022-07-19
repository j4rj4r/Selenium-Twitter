from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

class Driver:
    def __init__(self, profile):
        self.profile = profile
        self.chrome_options = None
        self.driver = None
        self.action = None

    def setup(self, log_path='./logs/', OperatingSystem='linux'):
        self.chrome_options = Options()

        # Anti bot detection
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.chrome_options.add_experimental_option('useAutomationExtension', False)
        self.chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        # detach the browser from the terminal
        self.chrome_options.add_experimental_option("detach", True)


        # Language Browser
        self.chrome_options.add_argument('--lang=fr-FR')

        # Maximize Browser
        self.chrome_options.add_argument('--start-maximized')

        # Disable infobars
        self.chrome_options.add_argument('disable-infobars')
        
        # Disable save password
        prefs = {'credentials_enable_service': False,
                'profile.password_manager_enabled': False}
        self.chrome_options.add_experimental_option('prefs', prefs)

        # Set profile
        self.chrome_options.add_argument(f'user-data-dir=./Profiles/{self.profile}')

        self.driver = webdriver.Chrome(f'./ChromeDriver/{OperatingSystem}/chromedriver',options=self.chrome_options, service_args=[f'--log-path={log_path}ChromeDriver.log'])
        self.action = ActionChains(self.driver)
        return self.driver, self.action
    
    def get_driver(self):
        return self.driver
    
    def get_action(self):
        return self.action