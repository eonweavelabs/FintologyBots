from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# bay view funding
# -----------------------------------------------------------------

def bayviewfunding(driver, data, product_id):
    try:
        driver.get("https://www.bayviewfunding.com/")
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        companyName = data.get("personal").get("companyName")
        email = data.get("email")
        phoneNumber = data.get("personal").get("mobileNumber")
        city = data.get("personal").get("city")
        state = data.get("personal").get("state")

        random_sleep(20)

        # First Name
        write_delay(driver, '//*[@id="firstname-daa0ec2e-3431-4a5e-a527-27fd4a285596_4176"]', firstName)
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="lastname-daa0ec2e-3431-4a5e-a527-27fd4a285596_4176"]', lastName)
        random_sleep(1)

        # Company Name
        write_delay(driver, '//*[@id="company-daa0ec2e-3431-4a5e-a527-27fd4a285596_4176"]', companyName)
        random_sleep(1)

        # Email
        write_delay(driver, '//*[@id="email-daa0ec2e-3431-4a5e-a527-27fd4a285596_4176"]', email)
        random_sleep(1)

        # Phone Number
        write_delay(driver, '//*[@id="phone-daa0ec2e-3431-4a5e-a527-27fd4a285596_4176"]', phoneNumber)
        random_sleep(1)

        # City
        write_delay(driver, '//*[@id="city-daa0ec2e-3431-4a5e-a527-27fd4a285596_4176"]', city)
        random_sleep(1)

        # State/Region
        write_delay(driver, '//*[@id="state-daa0ec2e-3431-4a5e-a527-27fd4a285596_4176"]', state)


        random_sleep(2)

        # Apply Now button
        send_click(driver, '//*[@id="hsForm_daa0ec2e-3431-4a5e-a527-27fd4a285596_4176"]/div/div[2]/input')
        random_sleep(15)

        full_name = f"{firstName} {lastName}"
        card_name = "bay view funding"
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
        full_name = f"{data.get('personal').get('firstName')} {data.get('personal').get('lastName')}"
        card_name = "bay view funding"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
