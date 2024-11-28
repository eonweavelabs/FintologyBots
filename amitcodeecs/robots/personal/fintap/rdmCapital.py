from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# ------------------------------------------------------
# Fintap Rdm Capital
# ------------------------------------------------------

def fintapRdmCapital(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Neha",
        #         "lastName": "lastName",
        #         "dob": "10/06/2000",
        #         "mobileNumber": 7349303040,
        #         "homeAddress": "123 street",
        #         "city": "Jaipur",
        #         "state": "AK",
        #         "zipcode": 85445,
        #         "grossIncome": 876655,
        #         "desiredCapital": 50000,
        #         "capitalAdvanceStart": "Immediately (less than 1 week)",
        #         "capitalPurpose": "Inventory",
        #         "businessName": "My Business",
        #         "businessStartMonth": "January",
        #         "businessStartYear": 2010,
        #         "industry": "Retail"
        #     }
        # }
        driver.get("https://www.fintap.com/apply-now/")
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        dob = data.get("personal").get("dob")
        homeAddress = data.get("personal").get("homeAddress")
        city = data.get("personal").get("city")
        zipcode = data.get("personal").get("zipcode")
        state = data.get("personal").get("state")
        email = data.get("email")
        mobileNumber = data.get("personal").get("mobileNumber")
        grossIncome = data.get("personal").get("householdIncome")
        desiredCapital = data.get("personal").get("desiredCapital")
        capitalAdvanceStart = data.get("personal").get("capitalAdvanceStart")
        capitalPurpose = data.get("personal").get("capitalPurpose")
        businessName = data.get("personal").get("businessName")
        businessStartMonth = data.get("personal").get("businessStartMonth")
        businessStartYear = data.get("personal").get("businessStartYear")
        industry = data.get("personal").get("industry")

        random_sleep(20)
        
         # Desired Capital
        write_delay(driver, '//*[@id="input_1_5"]', desiredCapital)
        random_sleep(1)

        # Capital Advance Start
        send_click(driver, '//*[@id="label_1_6_0"]')
        # if capitalAdvanceStart == "Immediately (less than 1 week)":
        #     send_click(driver, '//*[@id="choice_1_6_0"]')
        # elif capitalAdvanceStart == "Within 30-60 days":
        #     send_click(driver, '//*[@id="choice_1_6_1"]')
        # elif capitalAdvanceStart == "Within 60-90 days":
        #     send_click(driver, '//*[@id="choice_1_6_2"]')
        # elif capitalAdvanceStart == "90+ days":
        #     send_click(driver, '//*[@id="choice_1_6_3"]')
        random_sleep(1)

        # Capital Purpose
        send_click(driver, '//*[@id="label_1_7_1"]')
        # if capitalPurpose == "Inventory":
        #     send_click(driver, '//*[@id="choice_1_7_0"]')
        # elif capitalPurpose == "Cash flow":
        #     send_click(driver, '//*[@id="choice_1_7_1"]')
        # elif capitalPurpose == "Expansion":
        #     send_click(driver, '//*[@id="choice_1_7_2"]')
        # elif capitalPurpose == "Equipment purchase":
        #     send_click(driver, '//*[@id="choice_1_7_3"]')
        # elif capitalPurpose == "Sales / Marketing":
        #     send_click(driver, '//*[@id="choice_1_7_4"]')
        # elif capitalPurpose == "Other":
        #     send_click(driver, '//*[@id="choice_1_7_5"]')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="gform_next_button_1_9"]')
        random_sleep(1)


        # First Name
        write_delay(driver, '//*[@id="input_1_28"]', firstName)
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="input_1_29"]', lastName)
        random_sleep(1)

        # Email
        write_delay(driver, '//*[@id="input_1_11"]', email)
        random_sleep(1)

        # Phone number
        write_delay(driver, '//*[@id="input_1_12"]', mobileNumber)
        random_sleep(1)
        
        # Continue
        send_click(driver, '//*[@id="gform_next_button_1_14"]')
        random_sleep(1)


        # Business Name
        write_delay(driver, '//*[@id="input_1_15"]', businessName)
        random_sleep(1)

        # Business Start Month
        write_delay(driver, '//*[@id="input_1_30"]', businessStartMonth)
        random_sleep(1)

        # Business Start Year
        write_delay(driver, '//*[@id="input_1_20"]', businessStartYear)
        random_sleep(1)

        # Monthly Revenue
        write_delay(driver, '//*[@id="input_1_21"]', grossIncome)
        random_sleep(1)

        # Industry
        send_click(driver, '//*[@id="label_1_22_2"]')
        # if industry == "Restaurants":
        #     send_click(driver, '//*[@id="choice_1_22_0"]')
        # elif industry == "Construction":
        #     send_click(driver, '//*[@id="label_1_22_1"]]')
        # elif industry == "Retail":
        #     send_click(driver, '//*[@id="choice_1_22_2"]')
        # elif industry == "Auto Repair":
        #     send_click(driver, '//*[@id="choice_1_22_3"]')
        # elif industry == "Transportation":
        #     send_click(driver, '//*[@id="choice_1_22_4"]')
        # elif industry == "Professional Services":
        #     send_click(driver, '//*[@id="choice_1_22_5"]')
        # elif industry == "HealthCare":
        #     send_click(driver, '//*[@id="choice_1_22_6"]')
        # elif industry == "Other":
        #     send_click(driver, '//*[@id="choice_1_22_7"]')
        random_sleep(1)

        # I'm not a robot
        send_click(driver, '//*[@id="recaptcha-anchor"]')
        random_sleep(1)

        # Complete
        send_click(driver, '//*[@id="gform_submit_button_1"]')
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Fintap Rdm Capital"
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
        card_name = "Fintap Rdm Capital"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
