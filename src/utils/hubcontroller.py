from selenium import webdriver


class HubController:
    def __init__(self) -> None:
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_argument("--kiosk")
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--no-sandbox")
        self.chrome_driver = None

    def open_url(self, url: str) -> None:
        if self.chrome_driver is not None:
            del self.chrome_driver

        self.chrome_driver = webdriver.Chrome(options=self.options)
        self.chrome_driver.get(url)

    def is_browser_open(self) -> bool:
        try:
            self.chrome_driver.current_url
            return True
        except:
            return False
