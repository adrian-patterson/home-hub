from selenium import webdriver


class HubController:
    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("useAutomationExtension", False)
        self.chrome_options.add_experimental_option(
            "excludeSwitches", ["enable-automation"]
        )
        self.chrome_options.add_argument("--kiosk")
        self.chrome_driver = None

    def open_url(self, url: str) -> None:
        if self.chrome_driver is not None:
            del self.chrome_driver

        self.chrome_driver = webdriver.Chrome(options=self.chrome_options)
        self.chrome_driver.get(url)

    def is_browser_open(self) -> bool:
        try:
            self.chrome_driver.current_url
            return True
        except:
            return False
