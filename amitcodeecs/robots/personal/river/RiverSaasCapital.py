from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------
# River Saas Capital
# -----------------------------------------------------

def riverSaasCapital(driver, data, product_id):
    try:
        #data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Krishan Pratap",
        #         "lastName": "lastName",
        #         "jobTitle": "CEO",
        #         "company": "My Business Name",
        #         "website": "https://mybusiness.com",
        #         "city": "Jaipur",
        #         "state": 'AK',
        #         "mrr": 546843,
        #         "additionalComments": "No comments"
        #     }
        # }

        email = data.get("email")
        personal = data.get("personal")
        firstName = personal.get("firstName")
        lastName = personal.get("lastName")
        jobTitle = personal.get("jobTitle")
        company = personal.get("company")
        website = personal.get("website")
        city = personal.get("city")
        state = personal.get("state")
        mrr = personal.get("mrr")
        additionalComments = personal.get("additionalComments")

        driver.get("https://riversaascapital.com/apply/")
        random_sleep(20)

        # --------------------
        # Fill the form
        # --------------------
        
        driver.switch_to.frame(0)
        
        write_delay(driver, '//*[@id="input_3"]', firstName)
        random_sleep(2)
        write_delay(driver, '//*[@id="input_4"]', lastName)
        random_sleep(2)
        write_delay(driver, '//*[@id="input_20"]', jobTitle)
        random_sleep(2)
        write_delay(driver, '//*[@id="input_5"]', email)
        random_sleep(2)
        write_delay(driver, '//*[@id="input_7"]', company)
        random_sleep(2)
        driver.switch_to.frame(0)
        random_sleep(2)
        send_click(driver, '//*[@id="_label"]')
        driver.switch_to.default_content()
        driver.switch_to.frame(0)
        random_sleep(2)
        write_delay(driver, '//*[@id="input_16"]', website)
        random_sleep(2)
        write_delay(driver, '//*[@id="input_19_city"]', city)
        random_sleep(2)
        write_delay(driver, '//*[@id="input_19_state"]', state)
        random_sleep(2)
        # write_delay(driver, '//*[@id="input_8"]', mrr)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(by=By.XPATH,value='//*[@id="input_8"]')
                select = Select(select_element)
                select.select_by_value('$50K-$140K') 
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(2)
        write_delay(driver, '//*[@id="input_9"]', additionalComments)
        random_sleep(2)
        driver.switch_to.frame(0)
        send_click(driver, '//*[@id="_label"]')
        random_sleep(2)
        send_click(driver, '//*[@id="userInput"]')
        random_sleep(2)
        driver.switch_to.default_content()
        driver.switch_to.frame(0)
        send_click(driver, '//*[@id="input_2"]')

        # ------------------------
        # Handle confirmation
        # ------------------------

        retry_count = 0
        while retry_count < 600:
            try:
                driver.find_element(by=By.XPATH, value='//*[@id="CONFIRMATION_ADVISORY"]')
                break
            except:
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        full_name = firstName + " " + lastName
        card_name = "River SaaS Capital"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)

    except:
        traceback.print_exc()
        input("Error in application")
        full_name = firstName + " " + lastName
        card_name = "River SaaS Capital"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
