import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "/Users/CarlosMartinez/Desktop/Coding/chromedriver"
url = "https://www.linkedin.com/jobs/search/?currentJobId=3154580133&distance=25.0&f_AL=true&f_WT=2&geoId=103644278&keywords=easy%20apply&location=United%20States®"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)
#Login Initialization
sign_in_btn = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_btn.click()
time.sleep(4)
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("cmartinez2123@gmail.com")
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("Sfgiants1!")
sign_in_btn_2 = driver.find_element(By.CLASS_NAME, "btn__primary--large")
sign_in_btn_2.click()
time.sleep(5)

#Get list of Job Listings
job_listings = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")

def apply():
    try:
        jobs_apply_btn = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
    except NoSuchElementException:
        return
    jobs_apply_btn.click()
    time.sleep(5)
    next_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button')
    next_btn.click()
    time.sleep(3)
    review_btn = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]")
    review_btn.click()
    time.sleep(2)
    follow_btn = driver.find_element(By.CLASS_NAME, "ember-checkbox")
    driver.execute_script('arguments[0].click()', follow_btn)
    submit_application = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]")
    submit_application.click()
    time.sleep(3)

for job in job_listings:
    job.click()
    time.sleep(2)
    apply()

