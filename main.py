from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
PROMISED_DOWN = float(os.getenv("PROMISED_DOWN"))
PROMISED_UP = float(os.getenv("PROMISED_UP"))
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
ISP_EMAIL = os.getenv("ISP_EMAIL")

class InternetSpeedBot:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 60)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        try:
            self.driver.get("https://www.speedtest.net/")
            accept_button = self.wait.until(ec.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
            accept_button.click()

            activate_test_button = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".start-text")))
            activate_test_button.click()

            self.wait.until(lambda d: (d.find_element(By.CSS_SELECTOR, "span.download-speed").text not in ("", "—") and d.find_element(By.CSS_SELECTOR, "span.upload-speed").text not in ("", "—")))

            upload_text = self.driver.find_element(By.CSS_SELECTOR, value="span.result-data-large.number.result-data-value.upload-speed").text
            download_text = self.driver.find_element(By.CSS_SELECTOR, value="span.result-data-large.number.result-data-value.download-speed").text
            self.up = float(upload_text.strip())
            self.down = float(download_text.strip())

        finally:
            self.driver.quit()

        # --- Legacy Feature (Disabled) ---
        # Originally, this project attempted to automate posting to X (Twitter)
        # using Selenium. Due to platform anti-bot protections and login flow
        # instability, this approach was replaced with an SMTP email alert system.
    def tweet_at_provider(self):
        pass

    def send_email_alert(self):
        message = f"Internet speed is below the promised threshold.\n\nExpected Download: {PROMISED_DOWN} Mbps\nExpected Upload: {PROMISED_UP} Mbps\n\nActual Download: {self.down} Mbps\nActual Upload: {self.up} Mbps"

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL_ADDRESS,
                    to_addrs=ISP_EMAIL,
                    msg=f"Subject: 🚨Internet Speed Alert.\n\n{message}".encode("utf-8")
                )
                print(f"Download Speed: {self.down} Mbps")
                print(f"Upload Speed: {self.up} Mbps")
                print("🚨Internet Speed Alert sent")
        except Exception as e:
            print("❌ Failed to send email", e)


if __name__ == "__main__":
    bot = InternetSpeedBot()
    bot.get_internet_speed()
    if bot.up < PROMISED_UP or bot.down < PROMISED_DOWN:
        bot.send_email_alert()
    else:
        print("✅ Internet speed is within the expected range")
        print(f"Download Speed: {bot.down} Mbps")
        print(f"Upload Speed: {bot.up} Mbps")

