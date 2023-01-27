from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import random
import json
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException
from dotenv import load_dotenv
import os

load_dotenv()


def sleep_time():
    time_random = random.uniform(7, 15)
    return time_random


driver = webdriver.Firefox()

driver.get('https://www.upwork.com/ab/account-security/login')

email = os.environ['EMAIL']
password = os.environ['PASSWORD']

email_field = driver.find_element(By.ID, 'login_username')
email_button = driver.find_element(By.ID, "login_password_continue")
email_field.send_keys(email)

email_button.click()

time.sleep(sleep_time())

password_field = driver.find_element(By.ID, 'login_password')
password_field.send_keys(password)
login_button = driver.find_element(By.ID, "login_control_continue")

login_button.click()

time.sleep(sleep_time())

# search_box_div = driver.find_element('css selector',
#                                      ".up-input-group .up-input-group-clear")
# search_box = driver.find_element("css selector", "form")

# print(search_box.is_enabled())
# print(search_box.is_displayed())
# search_box.send_keys("javascript")
# search_box.send_keys(Keys.RETURN)

driver.get(
    'https://www.upwork.com/nx/jobs/search/?q=javascript&sort=recency&t=0,1&client_hires=1-9,10-&proposals=0-4,5-9&amount=500-999,1000-4999,5000-&hourly_rate=15-'
)

time.sleep(sleep_time())

all_jobs = driver.find_element("css selector", "div.up-card-section")
all_skills = all_jobs.find_elements("css selector", "div.up-skill-wrapper")
all_skills_a_tags = all_skills[0].find_elements("css selector", "a")

# for a_tag in all_skills_a_tags:
#     print(a_tag.text)

# print(all_skills, "all skills")
jobs = all_jobs.find_elements("css selector", "h3.job-tile-title")

# job_link = jobs[0].find_element("css selector", "a")
# html_link = job_link.get_attribute("href")

# parent_element = jobs[0].find_element(By.XPATH, "..")

# print(jobs[0], "jobbbababababa")

# print(jobs[0].is_displayed(), "jobs")

# jobs[0].click()

for i in range(1):
    jobs[i].click()
    time.sleep(sleep_time())

    danger_element = driver.find_elements("css selector", "span.ml-5")
    # print(danger_element)
    back_button = driver.find_element("css selector",
                                      'button[data-test="slider-go-back"]')
    if len(danger_element) > 0:
        print("danger elem")
        #     back_button.click()
        #     time.sleep(sleep_time())
        #     continue

        # else:
        # print("else statement")
        current_url = json.dumps(driver.current_url)

        # activity_on_job = driver.find_element("css selector", "div.col-lg-6")
        client_info = driver.find_element("css selector",
                                          "div.cfe-ui-job-about-client")

        posted_on = driver.find_element("css selector", "#posted-on")

        all_sections = driver.find_elements("css selector",
                                            "section.up-card-section")

        activity_on_job = driver.find_element(
            "css selector", "div[data-test='client-activity']")

        activity_on_job_list = activity_on_job.find_elements(
            "css selector", "li")

        for activity_on_job_element in activity_on_job_list:
            span_element = activity_on_job_element.find_elements(
                "css selector", "span")
            span_element_2 = span_element[1].find_element(
                By.XPATH, "//span[not(node())]")
            # span_element[1].find_element(
            #     "css selector", "span")

            print(span_element[0].text)
            print(span_element_2.text)

        # print(activity_on_job, "activity on job")
        # print(client_info, " client info")
        # print(posted_on, " posted on")
        # print(all_sections, " all sections")

        # print(client_activity, " client_activity")

        # for sections in all_sections:
        #     try:
        #         skills_and_expertise = sections.find_element(
        #             "css selector", "h4:contains('Skills and Expertise')")

        #         skills_and_expertise_parent_element = skills_and_expertise.find_element(
        #             By.XPATH, "..")

        #     except NoSuchElementException:
        #         continue

        with open("links.txt", 'w') as f:
            f.write(current_url)

        back_button.click()
        time.sleep(sleep_time())

# print(danger_element[0].is_displayed())

# back_button = driver.find_element("css selector", "button.up-slider-prev-btn")
# print(parent_element.is_enabled())
# print(parent_element.location_once_scrolled_into_view)

# all_jobs = driver.find_elements("css selector", ".up-card-list-section")

# jobs_values = json.dumps(all_jobs)

# element_text = json_values.text

# Convert the element text to a dictionary
# data = {'element_text': element_text}

# with open("jobs.txt", " w") as f:
#     f.write(data)