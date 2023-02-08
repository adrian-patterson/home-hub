from selenium import webdriver


class HubController:
    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("useAutomationExtension", False)
        self.chrome_options.add_experimental_option(
            "excludeSwitches", ["enable-automation"]
        )
        self.chrome_options.add_argument("--kiosk")
        self.chrome_options.add_argument("disable-infobars")
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_driver = None

    def open_url(self, url: str) -> None:
        new_driver = webdriver.Chrome(options=self.chrome_options)
        new_driver.get(url)

        if self.chrome_driver is not None:
            del self.chrome_driver

        self.chrome_driver = new_driver

    def is_browser_open(self) -> bool:
        try:
            self.chrome_driver.current_url
            return True
        except:
            return False

    def close_browser(self) -> None:
        if self.chrome_driver is not None:
            del self.chrome_driver
