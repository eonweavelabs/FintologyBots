from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# ------------------------------------------------------
# Founders First Capital Partners
# ------------------------------------------------------

def FFCPartners(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Neha",
        #         "lastName": "lastName",
        #         "businessName": "My Business",
        #         "businessPhone": 7349303040,
        #         "businessWebsite": "https://mybusiness.com",
        #         "yearFounded": "2010",
        #         "businessZipCode": 85445,
        #         "annualRevenueLastYear": 876655,
        #         "annualRevenueTwoYearsAgo": 765432,
        #         "isProfitable": "yes",
        #         "financingInterestLevel": "high",
        #         "revenueStreams": "both"
        #     }
        # }
        driver.get("https://foundersfirstcapitalpartners.com/rbf-apply/")
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        email = data.get("email")
        businessName = data.get("personal").get("businessName")
        businessPhone = data.get("personal").get("businessPhone")
        businessWebsite = data.get("personal").get("businessWebsite")
        yearFounded = data.get("personal").get("yearFounded")
        businessZipCode = data.get("personal").get("businessZipCode")
        annualRevenueLastYear = data.get("personal").get("annualRevenueLastYear")
        annualRevenueTwoYearsAgo = data.get("personal").get("annualRevenueTwoYearsAgo")
        isProfitable = data.get("personal").get("isProfitable")
        financingInterestLevel = data.get("personal").get("financingInterestLevel")
        revenueStreams = data.get("personal").get("revenueStreams")

        random_sleep(20)
        driver.switch_to.frame(0)
        # First Name
        write_delay(driver, '//*[@id="field127302278"]', firstName)
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="field127302279"]', lastName)
        random_sleep(1)

        # Business Email
        write_delay(driver, '//*[@id="field127302323"]', email)
        random_sleep(1)

        # Business Phone
        write_delay(driver, '//*[@id="field127302356"]', businessPhone)
        random_sleep(1)

        # Business Name
        write_delay(driver, '//*[@id="field127302366"]', businessName)
        random_sleep(1)

        # Financing Interest Level
        # write_delay(driver, '//*[@id="field127302362"]', financingInterestLevel)
        random_sleep(1)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="field127302362"]'
                )
                select = Select(select_element)
                select.select_by_value('3 - Interested now, please contact me')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Continue Application
        send_click(driver, '//*[@id="fsSubmitButton4869186"]')
        random_sleep(10)

        # ----------------------
        # p = 2
        # ----------------------
        # Business Website
        write_delay(driver, '//*[@id="field127303820"]', businessWebsite)
        random_sleep(1)

        # Year Business was Founded
        write_delay(driver, '//*[@id="field127303821"]', yearFounded)
        random_sleep(1)

        # Business ZIP Code
        write_delay(driver, '//*[@id="field127303822"]', businessZipCode)
        random_sleep(1)

        # Types of Business Revenue Streams
        if revenueStreams == "B2C":
            send_click(driver, '//*[@id="field127303823_1"]')
        elif revenueStreams == "B2B":
            send_click(driver, '//*[@id="field127303823_2"]')
        else:
            send_click(driver, '//*[@id="field127303823_3"]')
        random_sleep(1)

        # Continue Application
        send_click(driver, '//*[@id="fsSubmitButton4869224"]')
        random_sleep(1)
        
        # -----------------------
        # P = 3
        # -----------------------

        # Annual Revenue Last Year
        # write_delay(driver, '//*[@id="field127351655"]', annualRevenueLastYear)
        random_sleep(1)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="field127351655"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                select = Select(select_element)
                select.select_by_value('$5M or more')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Annual Revenue Two Years Ago
        # write_delay(driver, '//*[@id="field127351656"]', annualRevenueTwoYearsAgo)
        random_sleep(1)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="field127351656"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                select = Select(select_element)
                select.select_by_value('$5M or more')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Is Company Profitable
        # write_delay(driver, '//*[@id="field127351654"]', isProfitable)
        random_sleep(1)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="field127351654"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                select = Select(select_element)
                select.select_by_value('Yes')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Submit Application
        send_click(driver, '//*[@id="fsSubmitButton4870779"]')
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Founders First Capital Partners"
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
        card_name = "Founders First Capital Partners"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
