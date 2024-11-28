from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# ------------------------------------------------------
# Hsbc
# ------------------------------------------------------

def hsbc(driver, data, product_id):
    try:
        #data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Neha",
        #         "mobileNumber": 7349303040,
        #         "nearestBranch": "New York",
        #     }
        # }
        driver.get("https://hsbc.lsqportal.com/Premier")
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        mobileNumber = data.get("personal").get("mobileNumber")
        nearestBranch = data.get("personal").get("nearestBranch")
        email = data.get("email")

        random_sleep(20)

        # First Name
        write_delay(driver, '//*[@id="41323cb2-eb98-496e-be68-27cacc341790__tab1__section1__mx_Custom_1__Opportunity__12000"]', firstName)
        random_sleep(1)

        # Phone number
        write_delay(driver, '//*[@id="FF_41323cb2-eb98-496e-be68-27cacc341790__Phone__Lead__0"]/div/span[2]/div/input[2]', mobileNumber)
        random_sleep(1)

        # Nearest HSBC Branch
        write_delay(driver, '//*[@id="FF_41323cb2-eb98-496e-be68-27cacc341790_mx_Premier_Branch_CityLead_0"]/div/span[2]/div/div[2]/span/span[1]/span', nearestBranch)
        random_sleep(1)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="FF_41323cb2-eb98-496e-be68-27cacc341790__mx_Premier_Branch_City__Lead__0"]/div/span[2]/div/div[2]/span/span[1]/span')
                random_sleep(5)
                send_click(driver, '//*[@id="select2-4aiq-results"]/li[2]')
                random_sleep(2)
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="41323cb2-eb98-496e-be68-27cacc341790__tab1__section1__mx_Premier_Branch_City__Lead__0"]'
                )
                driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, 'Ahmedabad')
                   
                # select = Select(select_element)
                # select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Consent
        # send_click(driver, '//*[@id="FF_41323cb2-eb98-496e-be68-27cacc341790_mx_ConsentLead_0"]/div/span[2]/div/label/input')
        # random_sleep(1)

        # Submit
        send_click(driver, '//*[@id="lsq-form-modal"]/div[1]/div/div/div/div[3]/div[2]/button[2]')
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{firstName}"
        card_name = "Hsbc"
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
        full_name = f"{data.get('personal').get('firstName')}"
        card_name = "Hsbc"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
