from selenium import webdriver


class HubController:
    def __init__(self) -> None:
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument("--kiosk")
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--no-sandbox")
        self.firefox_driver = None

    def open_url(self, url: str) -> None:
        if self.firefox_driver is not None:
            del self.firefox_driver

        self.firefox_driver = webdriver.Firefox(options=self.options)
        self.firefox_driver.get(url)

    def is_browser_open(self) -> bool:
        try:
            self.firefox_driver.current_url
            return True
        except:
            return False
