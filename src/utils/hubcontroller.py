import os
import subprocess


class HubController:
    def __init__(self) -> None:
        self.browser_process: subprocess.Popen = None
        self.set_display_sleep_options()

    def set_display_sleep_options(self):
        # Don't allow display to sleep for the next 86400 seconds (24 hours)
        os.system("xset s 86400")
        os.system("xset dpms 86400 86400 86400")

    def open_url_kiosk_attached(self, url: str) -> None:
        if self.is_browser_open():
            self.browser_process.kill()

        self.browser_process = subprocess.Popen(
            f"exec chromium-browser {url} --kiosk --new-window --incognito",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

    def open_url_fullscreen_detached(self, url: str) -> None:
        subprocess.Popen(
            f"exec firefox {url} --start-maximized --new-window",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

    def close_browser(self) -> None:
        if self.is_browser_open():
            self.browser_process.kill()

    def is_browser_open(self) -> bool:
        if self.browser_process is not None:
            return True
        return False

    def sleep_display(self) -> None:
        os.system("xset dpms force off")

    def wake_up_display(self) -> None:
        os.system("xset dpms force on")
