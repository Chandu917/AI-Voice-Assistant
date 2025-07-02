import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException

class JobApplicationAutomator:
    def __init__(self, user_profile, resume_path, cover_letter_path=None):
        self.user_profile = user_profile
        self.resume_path = resume_path
        self.cover_letter_path = cover_letter_path
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=chrome_options)

    def apply_to_linkedin_job(self, job_url):
        try:
            self.driver.get(job_url)
            time.sleep(3)
            try:
                easy_apply_button = self.driver.find_element(By.CLASS_NAME, "jobs-apply-button")
                easy_apply_button.click()
                time.sleep(2)
            except NoSuchElementException:
                print("Easy Apply button not found.")
                return False

            # Fill application form - simplified example
            try:
                upload_resume = self.driver.find_element(By.XPATH, "//input[@type='file']")
                upload_resume.send_keys(self.resume_path)
                time.sleep(1)
            except NoSuchElementException:
                print("Resume upload field not found.")

            # Add cover letter if available
            if self.cover_letter_path:
                try:
                    cover_letter_field = self.driver.find_element(By.TAG_NAME, "textarea")
                    with open(self.cover_letter_path, "r") as f:
                        cover_letter_text = f.read()
                    cover_letter_field.send_keys(cover_letter_text)
                    time.sleep(1)
                except NoSuchElementException:
                    print("Cover letter field not found.")

            # Submit application
            try:
                submit_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
                submit_button.click()
                time.sleep(2)
                print("Application submitted successfully.")
                return True
            except NoSuchElementException:
                print("Submit button not found.")
                return False

        except WebDriverException as e:
            print(f"WebDriver error: {e}")
            return False

    def close(self):
        self.driver.quit()
