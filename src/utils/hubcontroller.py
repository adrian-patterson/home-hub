import os
from selenium import webdriver


class HubController:
    def __init__(self) -> None:
        # Initialize options which will give a clean full screen browser display
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
        self.chrome_driver: webdriver.Chrome = None

        # Don't allow display to sleep for the next 86400 seconds (24 hours)
        os.system("xset s 86400")
        os.system("xset dpms 86400 86400 86400")

    def open_url(self, url: str) -> None:
        if self.is_browser_open():
            self.chrome_driver.quit()

        self.chrome_driver = webdriver.Chrome(options=self.chrome_options)
        self.chrome_driver.get(url)

    def close_browser(self) -> None:
        if self.chrome_driver is not None:
            self.chrome_driver.quit()

    def is_browser_open(self) -> bool:
        try:
            self.chrome_driver.current_url
            return True
        except:
            return False

    def sleep_display(self) -> None:
        os.system("xset dpms force off")

    def wake_up_display(self) -> None:
        os.system("xset dpms force on")
